list_ = ["Collo", "Collo", "Mark", "Collo", "Lucy", "Collo", "Mark"]

record_dict = {}

for name in list_:
    record_dict[name] = record_dict.get(name, 0) + 1

# print(record_dict)

print('name is collo'.title())
print('name is collo'.upper())
print('name is collo'.capitalize())

print('name'.startswith('n'))

name = input('Input your name: ')
print(name)
from faker import Faker
fake = Faker()

print(fake.catch_phrase())
print(fake.sentence())
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask.ext.hybrid import hybrid_property
metadata = MetaData(
    naming_convention = {}
)
db = SQLAlchemy(metadata=metadata)


class Magazine(db.metadata):
    def __init__(self, name):
        id = db.Column(db.Integer, primary_key=True, unique=True)
        _password_hash = db.Column(db.String, nullable=False)

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        )
        self._password_hash = password_hash.decode('utf-8')
    def authenticate(self, password):
        bcrypt.check_password_hash(
            self.password_hash, password.encode('utf-8')
        )


    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = self.simple_hash(password)

    def authenticate(self, password):
        return self.simple_hash == self.simple_hash(password)
    @staticmethod
    def simple_hash(input):
       return str(bytearray(input, encoding='utf-8')) 
from flask_restful import Api, Resource

from flask import Flask, make_response
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magazines.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)
bcrypt = Bcrypt(app)

from app import bcrypt

import sqlite3

CONN = sqlite3.connect('app.db')
CURSOR = CONN.cursor()

arr = [("name", 'Anna'), ('alice', 'Zedd'), ('bakari', 'Mona'), ('mina', 'Nina')]
print(sorted(arr))
print(sorted(arr, key=lambda n: n[1]))
