import datetime
from marshmallow_model import Newsletter, db

from flask_marshmallow_hateoas import app

from faker import Faker

with app.app_context():
    fake = Faker()
    newsletters = [
        Newsletter(title=fake.catch_phrase(), body=fake.sentence())
        for _ in range(50)
    ]

    db.session.add_all(newsletters)

    db.session.commit()