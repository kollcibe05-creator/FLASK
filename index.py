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

metadata = MetaData(
    naming_convention = {}
)
db = SQLAlchemy(metadata=metadata)

class Magazine(db.metadata):
    def __init__(self, name):
        self.name = name

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