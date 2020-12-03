"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, make_response
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
