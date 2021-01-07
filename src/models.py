from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean, Text, Float, Table

db = SQLAlchemy()

written_by = Table("written_by", db.Model.metadata,
    Column("id_author", Integer, ForeignKey("author.id"), primary_key=True),
    Column("id_book", Integer, ForeignKey("book.id"), primary_key=True)
)

order_line = Table("order_line", db.Model.metadata,
    Column("id_book", Integer, ForeignKey("book.id"), primary_key=True),
    Column("id_order", Integer, ForeignKey("order.id"), primary_key=True)
)

follower = Table("follower", db.Model.metadata,
    Column("id_follower", Integer, ForeignKey("reader.id"), primary_key=True),
    Column("id_followed", Integer, ForeignKey("reader.id"), primary_key=True)
)

class Review(db.Model):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_reader = Column(Integer, ForeignKey("reader.id"), nullable=False, unique=False)
    id_book = Column(Integer, ForeignKey("book.id"), nullable=False, unique=False)
    stars = Column(Enum("1", "2", "3", "4", "5"), nullable=False)
    review = Column(Text(), nullable=True)
    # relations
    book_review = db.relationship("Book", back_populates="readers_reviews")
    reader_review = db.relationship("Reader", back_populates="books_reviews")

    def serialize(self):
        return {
            "id": self.id,
            "id_reader": self.id_reader,
            "id_book": self.id_book,
            "stars": self.stars,
            "review": self.review
        }

    def create(new_review):
        db.session.add(new_review)  
        db.session.commit()

    @classmethod
    def read_all(cls):
        get_all_reviews = Review.query.all()
        reviews = list(map(lambda x: x.serialize(), get_all_reviews))
        return reviews

class Shelf(db.Model):
    __tablename__= "shelf"
    id_reader = Column(Integer, ForeignKey("reader.id"), primary_key=True)
    id_book = Column(Integer, ForeignKey("book.id"), primary_key=True)
    shelf_name = Column(Enum("Comentados","Leídos","Favoritos","Pendientes","Comprados"), primary_key=True)
    # relations
    book_shelf = db.relationship("Book", back_populates="readers_shelves")
    reader_shelf = db.relationship("Reader", back_populates="books_shelves")

    @classmethod
    def read_all_shelves(cls):
        get_all_shelves = Shelf.query.all()
        shelves = list(map(lambda x: x.serialize(), get_all_shelves))
        return shelves

    def serialize(self):
        return {
            "id_reader": self.id_reader,
            "id_book": self.id_book,
            "shelf_name": self.shelf_name
        }

    @classmethod
    def read_by_reader_and_name(cls, shelf_name, reader_id):
        books_in_shelf = cls.query.filter_by(shelf_name = shelf_name, id_reader = reader_id)
        shelf = list(map(lambda x: x.serialize(), books_in_shelf))
        return shelf

    @classmethod
    def read_all_shelves(cls):
        shelves=Shelf.query.all()
        all_shelf=list(map(lambda x: x.serialize(), shelves))
        return all_shelf

    def add_book_to_shelf(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_book_on_shelf( id_reader, shelf_name, id_book ):
        book=Shelf.query.filter_by(id_reader=id_reader, shelf_name=shelf_name, id_book=id_book).first()
        db.session.delete(book)
        db.session.commit()
        return book

class Reader(db.Model):
    __tablename__= "reader"
    id = Column(Integer, primary_key=True)
    image = Column(Text(), nullable=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    is_active = Column(Boolean(), nullable=False)
    name = Column(String(255), nullable=True)
    description = Column(Text(), nullable=True)
    # relations
    orders = db.relationship("Order", lazy = True)
    books_reviews = db.relationship("Review", back_populates="reader_review")
    books_shelves = db.relationship("Shelf", back_populates="reader_shelf")
    readers = db.relationship("Reader", secondary=follower, primaryjoin=id == follower.c.id_follower, secondaryjoin=id == follower.c.id_followed, back_populates="readers")
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "description": self.description,
            "orders": self.orders
        }
    
    @classmethod
    def read_all(cls):
        readers = Reader.query.all()
        all_readers = list(map(lambda x: x.serialize(), readers))
        return all_readers

    def create(new_user):
        db.session.add(new_user)  
        db.session.commit()    

    def read_by_email(email):
        reader = Reader.query.filter_by(email=email).first()
        return reader

    def update(id_reader, name, description):
        reader_to_update = Reader.query.filter_by(id= id_reader).first()
        reader_to_update.name = name
        reader_to_update.description = description
        db.session.commit()
        return reader_to_update

class Book(db.Model):
    __tablename__= "book"
    id = Column(Integer, primary_key=True)
    image = Column(Text(), nullable=True)
    title = Column(String(120), nullable=False)
    synopsis = Column(Text(), nullable=False)
    format_type = Column(Enum("Tapa dura","Bolsillo","Ebook","Ilustrado","Tapa blanda"), nullable=False)
    genre = Column(Enum("Histórica","Romántica y erótica","Thriller","Ciencia ficción y fantástica","Biográfica","Juvenil","Novela gráfica", "Clásicos"), nullable=False)
    price = Column(Float(), nullable=False)
    # relations
    readers_reviews = db.relationship("Review", back_populates="book_review")
    readers_shelves = db.relationship("Shelf", back_populates="book_shelf")
    authors = db.relationship("Author", secondary=written_by, back_populates="books")
    orders = db.relationship("Order", secondary=order_line, back_populates="books")

    def serialize(self):
        return {
            "id": self.id,
            "image": self.image,
            "title": self.title,
            "synopsis": self.synopsis,
            "format_type": self.format_type,
            "genre": self.genre,
            "price": self.price
        }
    
    @classmethod
    def read_by_id(cls, book_id):
        book = Book.query.get(book_id)
        # all_books = list(map(lambda x: x.serialize(), book))
        return book.serialize()

    @classmethod
    def read_all(cls):
        all_books = Book.query.all()
        books = list(map(lambda x: x.serialize(), all_books))
        return books

    @classmethod
    def read_like_title(cls, title):
        books_by_title = Book.query.filter(Book.title.like(title)).all()
        books = list(map(lambda x: x.serialize(), books_by_title))
        return books

class Author(db.Model):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    biography = Column(Text(), nullable=False)
    image = Column(Text(), nullable=True)
    books = db.relationship("Book", secondary=written_by, back_populates="authors")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "biography": self.biography,
            "image": self.image,
        }
    
    @classmethod
    def read_all(cls):
        authors = cls.query.all()
        author = list(map(lambda x: x.serialize(), authors))
        return author
        
    @classmethod
    def read(cls, name_input):
        author = cls.query.filter_by(name = name_input)
        return author.serialize()

    @classmethod
    def read_like_author(cls, name):
        info_from_author = Author.query.filter(Author.name.like(name)).all()
        authors = list(map(lambda x: x.serialize(), info_from_author))
        return authors

class Order(db.Model):
    __tablename__= "order"
    id = Column(Integer, primary_key=True)
    final_price =  Column(Float(), nullable=False)
    reader_id = Column(Integer, ForeignKey("reader.id"))
    books = db.relationship("Book", secondary=order_line, back_populates="orders")

    def serialize(self):
        return {
            "id": self.id,
            "final_price": self.username,
            "reader_id": self.reader_id
        }
