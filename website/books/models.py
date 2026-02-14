from ..extensions import db
from ..auth.models import Person

class Authors(Person):
    __tablename__ = 'authors'
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), primary_key=True)
    author_description = db.Column(db.String(10000))
    author_nationality = db.Column(db.String(30))
    books = db.relationship('Books', backref='author', cascade='all, delete-orphan')

    __mapper_args__ = {
        'polymorphic_identity':'author'
    }


class Books(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, index=True)
    author_id = db.Column(db.Integer,db.ForeignKey('author.person_id'))
    isbn = db.Column(db.Integer)
    publisher = db.Column(db.String(255))
    number_pages = db.Column(db.Integer)
    publication_date = db.Column(db.Date)
    book_description = db.Column(db.String(10000))
    price = db.Column(db.Numeric(6,2), nullable=False)

