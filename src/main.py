"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap, token_required
from admin import setup_admin
from models import db, Reader, Author, Book, Review, Order, Shelf
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

@app.route('/register', methods=['GET', 'POST'])
def register():  
    body = request.get_json()  

    hashed_password = generate_password_hash(body['password'], method='sha256')

    new_user = Reader(email=body['email'], password=hashed_password, is_active= True, username=body["username"]) 
    db.session.add(new_user)  
    db.session.commit()    

    return jsonify({'message': 'registered successfully'})

@app.route('/readers', methods=['GET'])
def get_all_readers():  
   
   readers = Reader.query.all() 

   result = []   

   for reader in readers:   
       reader_data = {}   
       reader_data['id'] = reader.id  
       reader_data['email'] = reader.email 
       reader_data["username"] = reader.username
       reader_data["name"] = reader.name
       reader_data["description"] = reader.description
       
       result.append(reader_data)   

   return jsonify(result)

@app.route('/<reader_id>/<shelf_name>/books', methods=['GET'])
def get_all_shelves(reader_id, shelf_name):

    books_in_shelf = Shelf.read_by_reader_and_name(shelf_name, reader_id)
    print('Estanterias ', shelves)

    # books=[]

    # for book in books_in_shelf:
    #     read_by_id
    return jsonify(book_in_shelf), 200
    

@app.route('/authors', methods=['GET'])
def get_all_authors():
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

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
