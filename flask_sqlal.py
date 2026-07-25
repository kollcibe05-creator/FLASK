from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from sqlalchemy_serializer import SerializerMixin  # Serialization eg. to_dict()


metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Pet(db.Model, SerializerMixin):
    __tablename__ = "pets"

    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, index=True)
    species = db.Column(db.String, nullable=False)
    # verified = db.Column(db.Boolean, default=False) # for demo on constraints
    def __repr__(self):
        return f"<Pet {self.id}, {self.name}, {self.species}>" # 