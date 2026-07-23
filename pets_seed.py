from faker import Faker
from random import choice as rc

from db_intergration_sqlal import app
from flask_sqlal import db, Pet

with app.app_context():
    fake = Faker()

    Pet.query.delete()

    pets = []

    species = ["Dog", "Cat", "Chicken", "Hamster", "Turtle"]

    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    db.session.add_all(pets)
    db.session.commit()
