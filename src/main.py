"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, make_response, request
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS, cross_origin
from utils import APIException, generate_sitemap, token_required
from admin import setup_admin
from models import db, Reader, Author, Book, Review, Order, Shelf, written_by, follower
from init_database import init_db
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY']= os.environ.get("FLASK_APP_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)

CORS(app)
setup_admin(app)
app.cli.add_command(init_db)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/register', methods=['POST'])
def register():  
    body = request.get_json()  

    hashed_password = generate_password_hash(body["password"], method="sha256")

    new_user = Reader(email=body['email'], password=hashed_password, is_active= True, username=body["username"])

    Reader.create(new_user)

    return jsonify({'message': 'registered successfully'}), 200

@app.route("/login", methods=["GET", "POST"])
def login():
    body = request.get_json()
    
    if "x-access-tokens" not in request.headers:
        if not body or not body["email"] or not body["password"]:
            return make_response("El email o la contraseña no son correctas"), 401

        reader = Reader.read_by_email(body["email"])

        if check_password_hash(reader.password, body["password"]):
            token = jwt.encode({'id': reader.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token' : token.decode('UTF-8')}), 200

        return make_response("Error de login", 401)

    else:
        return make_response("Token válido", 200)

@app.route('/readers', methods=['GET'])
def get_all_readers():  
    readers = Reader.read_all() 
    result = []

    for reader in readers:
        reader_data = {}   
        reader_data['id'] = reader["id"]  
        reader_data['email'] = reader["email"] 
        reader_data["username"] = reader["username"]
        reader_data["name"] = reader["name"]
        reader_data["description"] = reader["description"]
       
        result.append(reader_data)   

    return jsonify(result)

@app.route('/books', methods=['GET'])
@cross_origin()
def get_all_books(): 
    args = request.args
    if "title" in args:
        title = args["title"]
        title = f"%{title}%"
        book = Book.read_like_title(title)
        return jsonify(book), 200
    else:
        books = Book.read_all()
        authors = Author.read_all()
        books_written_by_authors = db.session.query(written_by).all()
        result = []   
        for book_author in books_written_by_authors:
            for book in books:
                for author in authors:
                    if book["id"] == book_author[1]:
                        if author["id"] == book_author[0]:
                            book_data = {}   
                            book_data['id'] = book["id"] 
                            book_data['title'] = book["title"] 
                            book_data["image"] = book["image"]
                            book_data["synopsis"] = book["synopsis"]
                            book_data["format_type"] = book["format_type"]
                            book_data["genre"] = book["genre"]
                            book_data["price"] = book["price"]
                            book_data["id_author"] = author["id"]
                            book_data["name_author"] = author["name"]
                
                            result.append(book_data)
        return jsonify(result)
    
@app.route('/<reader_id>/<shelf_name>/books', methods=['GET'])
@cross_origin()
def get_all_shelves(reader_id, shelf_name):
    books_in_shelf = Shelf.read_by_reader_and_name(shelf_name, reader_id)

    books=[]
    for book in books_in_shelf:
        books.append(Book.read_by_id(book['id_book']))
    return jsonify(books), 200

@app.route('/shelves_by_id', methods=['GET'])
def read_all_shelves():
    try:
        shelves=Shelf.read_all_shelves()
        return jsonify(shelves), 200
    except:
        return 'not found', 400

@app.route('/<int:reader_id>/<shelf_name>/<int:book_id>', methods=['POST'])
@cross_origin()
def add_to_shelf(reader_id,shelf_name,book_id):

    new_book_in_shelf=Shelf(id_reader=reader_id, shelf_name=shelf_name, id_book=book_id)

    new_book_in_shelf.add_book_to_shelf()

    return jsonify(new_book_in_shelf.serialize())

@app.route('/<id_reader>/<shelf_name>/<id_book>' , methods=['DELETE'])
@cross_origin()
def delete_book_of_shelf(id_reader,shelf_name,id_book):
    delete_book = Shelf.delete_book_on_shelf(id_reader, shelf_name, id_book)
    print("libro borrado, ", delete_book)
    if delete_book is None:
        return "Do not found book in this shelf", 400
    else: 
        return delete_book.serialize(), 200
        
@app.route('/authors', methods=['GET'])
def get_all_authors():
    args = request.args
    if "name" in args:
        name = args["name"]
        name = f"%{name}%"
        author = Author.read_like_author(name)
        return jsonify(author), 200
    else:
        try:
            all_authors = Author.read_all()
            return jsonify(all_authors), 200
        except:
            return "Do not found authors", 400

@app.route("/author/<name_input>", methods=["GET"])
def get_author(name_input):
    try:
        author = Author.read(name_input)
        return jsonify(author), 200
    except:
        return "Author not found", 400

@app.route("/profile", methods=["GET"])
def get_shelves():
    all_shelves = Shelf.read_all_shelves()
    if all_shelves:
        return jsonify(all_shelves), 200
    else:
        return "Self not found", 400

@app.route('/profile/<int:id_reader>', methods=['PUT'])
# @token_required
def update_reader(id_reader):
    body=request.get_json()
    reader_to_update = Reader.update(id_reader, body["name"], body["description"])
    if reader_to_update:
        return reader_to_update.serialize()
    else:
        return "Couldn't update reader information", 404

@app.route('/reviews', methods=['GET'])
def get_all_reviews():  
    reviews = Review.read_all()
    readers = Reader.read_all()

    result = []   

    for review in reviews:
        for reader in readers:
            if reader["id"] == review["id_reader"]:
                review_data = {}   
                review_data['id'] = review["id"] 
                review_data['id_reader'] = review["id_reader"] 
                review_data["id_book"] = review["id_book"]
                review_data["stars"] = review["stars"]
                review_data["review"] = review["review"]
                review_data["username"] = reader["username"]
       
                result.append(review_data)
    
    return jsonify(result)

@app.route('/add_review', methods=['POST'])
def add_review():  
    body = request.get_json()  

    new_review = Review(id_reader=body['id_reader'], id_book=body["id_book"], stars=body["stars"], review=body["review"])

    Review.create(new_review)

    return jsonify({'message': 'Review created correctly'}), 200

@app.route("/following/<int:id_user_logged>", methods=["POST"])
def add_follower(id_user_logged):
    body=request.get_json()
    statement = follower.insert().values(id_follower=id_user_logged, id_followed=body["id_followed"])
    db.session.execute(statement)
    db.session.commit()
    return jsonify({"message": "Logged user is following a new user!"}), 200

@app.route("/following_followed", methods=["GET"])
@cross_origin()
def read_followers():
    readers = Reader.read_all()
    followers = db.session.query(follower).all()
    each_data = []
    result = []
    for each_follower in followers:
        for reader in readers:
            follower_data = {}
            follower_username = Reader.read_username_by_id(each_follower[0])
            if reader["id"] == each_follower[1]:
                follower_data["id_followed"] = each_follower[1]
                follower_data["username_followed"] = reader["username"]
                follower_data["id_follower"] = each_follower[0]
                follower_data["username_follower"] = follower_username
            
                result.append(follower_data)

    return jsonify(result)



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
