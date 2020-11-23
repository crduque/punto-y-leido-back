from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean, Text, Float, Table

db = SQLAlchemy()

written_by = Table("written_by", db.Model.metadata,
    Column("id_author", Integer, ForeignKey("author.id")),
    Column("id_book", Integer, ForeignKey("book.id"))
)

order_line = Table("order_line", db.Model.metadata,
    Column("id_book", Integer, ForeignKey("book.id")),
    Column("id_order", Integer, ForeignKey("order.id"))
)

follower = Table("follower", db.Model.metadata,
    Column("id_follower", Integer, ForeignKey("reader.id")),
    Column("id_followed", Integer, ForeignKey("reader.id"))
)

class Review(db.Model):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True)
    id_reader = Column(Integer, ForeignKey("reader.id"), primary_key=True)
    id_book = Column(Integer, ForeignKey("book.id"), primary_key=True)
    stars = Column(Enum("1", "2", "3", "4", "5"), nullable=False)
    review = Column(Text(), nullable=True)
    # relations
    book = db.relationship("book", back_populates="readers_reviews")
    reader = db.relationship("reader", back_populates="books_reviews")

    def serialize(self):
        return {
            "id": self.id,
            "id_reader": self.id_reader,
            "id_book": self.id_book,
            "stars": self.stars,
            "review": self.review
        }
    
    def read_all():
        reviews = Review.query.all()
        return reviews.serialize()

    @classmethod
    def read_by_reader(cls, id_reader_input):
        review = Review.query.filter_by(id_reader = id_reader_input)
        return review.serialize()

    @classmethod
    def read_by_book(cls, id_book_input):
        review = Review.query.filter_by(id_book = id_book_input)
        return review.serialize()

class Shelf(db.Model):
    __tablename__= "shelf"
    id_reader = Column(Integer, ForeignKey("reader.id"), primary_key=True)
    id_book = Column(Integer, ForeignKey("book.id"), primary_key=True)
    shelf_name = Column(Enum("Comentados","Leídos","Favoritos","Pendientes","Comprados"), nullable=False)
    # relations
    book = db.relationship("book", back_populates="readers_shelves")
    reader = db.relationship("reader", back_populates="books_shelves")

    def serialize(self):
        return {
            "id_reader": self.id_reader,
            "id_book": self.id_book,
            "shelf_name": self.shelf_name
        }
    
    def read_all():
        shelves = Shelf.query.all()
        return shelves.serialize()

    @classmethod
    def read(cls, id_reader_input):
        shelf = Shelf.query.filter_by(id_reader = id_reader_input)
        return shelf.serialize()

class Reader(db.Model):
    __tablename__= "reader"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    is_active = Column(Boolean(), nullable=False)
    name = Column(String(255), nullable=True)
    description = Column(Text(), nullable=True)
    # relations
    orders = db.relationship("order", lazy = True)
    books_reviews = db.relationship("review", back_populates="reader")
    books_shelves = db.relationship("shelf", back_populates="reader")
    readers = db.relationship("reader", secondary=follower, primaryjoin=id == follower.c.id_follower, secondaryjoin=id == follower.c.id_followed, back_populates="readers")
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "description": self.description,
            "orders": self.orders
        }

    def read_all():
        readers = Reader.query.all()
        return readers.serialize()

    @classmethod
    def read(cls, username_input):
        reader = Reader.query.filter_by(username = username_input)
        return reader.serialize()

class Book(db.Model):
    __tablename__= "book"
    id = Column(Integer, primary_key=True)
    image = Column(String(255), nullable=True)
    title = Column(String(120), nullable=False)
    synopsis = Column(Text(), nullable=False)
    format_type = Column(Enum("Tapa dura","Bolsillo","Ebook","Ilustrado","Tapa blanda"), nullable=False)
    genre = Column(Enum("Histórica","Romántica y erótica","Thriller","Ciencia ficción y fantástica","Biográfica","Juvenil","Novela gráfica", "Clásicos"), nullable=False)
    price = Column(Float(), nullable=False)
    # relations
    readers_reviews = db.relationship("review", back_populates="book")
    readers_shelves = db.relationship("shelf", back_populates="book")
    authors = db.relationship("author", secondary=written_by, back_populates="books")
    orders = db.relationship("order", secondary=order_line, back_populates="books")

    def serialize(self):
        return {
            "id": self.id,
            "image": self.username,
            "title": self.email,
            "synopsis": self.name,
            "format_type": self.description,
            "genre": self.genre,
            "price": self.price
        }
    
    def read_all():
        books = Book.query.all()
        return books.serialize()

    @classmethod
    def read(cls, title_input):
        book = Book.query.filter_by(title = title_input)
        return book.serialize()

class Author(db.Model):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    biography = Column(Text(), nullable=False)
    image = Column(String(255), nullable=True)
    books = db.relationship("book", secondary=written_by, back_populates="authors")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.username,
            "biography": self.email,
            "image": self.name,
        }
    
    def read_all():
        authors = Author.query.all()
        return authors.serialize()

    @classmethod
    def read(cls, name_input):
        author = Author.query.filter_by(name = name_input)
        return author.serialize()

class Order(db.Model):
    __tablename__= "order"
    id = Column(Integer, primary_key=True)
    final_price =  Column(Float(), nullable=False)
    reader_id = Column(Integer, ForeignKey("reader.id"))
    books = db.relationship("book", secondary=order_line, back_populates="orders")

    def serialize(self):
        return {
            "id": self.id,
            "final_price": self.username,
            "reader_id": self.reader_id
        }

    def read_all():
        orders = Order.query.all()
        return orders.serialize()

    @classmethod
    def read(cls, reader_id_input):
        order = Order.query.filter_by(reader_id = reader_id_input)
        return order.serialize()