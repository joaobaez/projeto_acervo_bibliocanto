from . import db
from flask_login import UserMixin



class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    type = db.Column(db.String(64))

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }


class Author(Person):
    __tablename__ = 'author'
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), primary_key=True)
    author_biography = db.Column(db.String(10000))
    books = db.relationship('Books', backref='author', cascade='all, delete-orphan')

    __mapper_args__ = {
        'polymorphic_identity':'author'
    }


class User(Person, UserMixin):
    __tablename__ = 'user'
    person_id =db.Column(db.Integer, db.ForeignKey('person.person_id'), primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }

    def get_id(self):
        return str(self.person_id)

class Admin(User):
    __tablename__ = 'admin'
    person_id = db.Column(db.Integer, db.ForeignKey('user.person_id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    author_id = db.Column(db.Integer,db.ForeignKey('author.person_id'))
    isbn = db.Column(db.Integer)
    publisher = db.Column(db.String(255))
    number_pages = db.Column(db.Integer)
    publication_date = db.Column(db.Date)
    description = db.Column(db.String(10000))
    price = db.Column(db.Numeric(6,2), nullable=False)


