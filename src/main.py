"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Reader, Author, Book, Review, Order, Shelf
from init_database import init_db

app = Flask(__name__)
app.url_map.strict_slashes = False
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

@app.route('/readers', methods=['GET'])
def get_all_readers():
    try:
        all_readers = Reader.read_all()
        return jsonify(all_readers), 200
    except:
        return "Do not found readers", 400

@app.route("/reader/<id_reader_input>", methods=["GET"])
def get_reader_by_id (id_reader_input):
    try:
        reader = Reader.read_by_reader(id_reader_input)
        return jsonify(reader), 200
    except:
        return "Reader not found", 400

@app.route("/reader/<id_book_input>", methods=["GET"])
def get_reader_by_id (id_book_input):
    try:
        reader = Reader.read_by_book(id_book_input)
        return jsonify(reader), 200
    except:
        return "Reader not found", 400
    
@app.route('/books', methods=['GET'])
def get_all_books():
    try:
        all_books = Book.read_all()
        return jsonify(all_books), 200
    except:
        return "Do not found books", 400

@app.route("/reader/<title_input>", methods=["GET"])
def get_book (title_input):
    try:
        book = Book.read(title_input)
        return jsonify(book), 200
    except:
        return "Book not found", 400

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

@app.route('/orders', methods=['GET'])
def get_all_orders():
    try:
        all_orders = Order.read_all()
        return jsonify(all_orders), 200
    except:
        return "Do not found orders", 400

@app.route("/order/<reader_id_input>", methods=["GET"])
def get_order(reader_id_input):
    try:
        order = Order.read(reader_id_input)
        return jsonify(order), 200
    except:
        return "Order not found", 400

@app.route('/reviews', methods=['GET'])
def get_all_reviews():
    try:
        all_reviews = Review.read_all()
        return jsonify(all_reviews), 200
    except:
        return "Do not found reviews", 400

@app.route("/review/<id_reader_input>", methods=["GET"])
def get_review(id_reader_input):
    try:
        review = Order.read(id_reader_input)
        return jsonify(review), 200
    except:
        return "Review not found", 400

@app.route('/shelves', methods=['GET'])
def get_all_shelves():
    try:
        all_shelves = Self.read_all()
        return jsonify(all_shelves), 200
    except:
        return "Do not found shelves", 400

@app.route("/shelf/<id_reader_input>", methods=["GET"])
def get_shelf(id_reader_input):
    try:
        shelf = Shelf.read(id_reader_input)
        return jsonify(shelf), 200
    except:
        return "Shelf not found", 400

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
