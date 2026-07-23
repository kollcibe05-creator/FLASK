from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData



metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Pet(db.Model):
    __tablename__ = "pets"

    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, index=True)
    species = db.Column(db.String, nullable=False)
    # verified = db.Column(db.Boolean, default=False) # for demo on constraints
