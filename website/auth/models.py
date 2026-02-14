from ..extensions import db
from flask_login import UserMixin


class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    type = db.Column(db.String(64))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'person'
    }


class User(Person, UserMixin):
    __tablename__ = 'user'
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), primary_key=True)
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
