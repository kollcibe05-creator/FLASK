import random
import datetime
from faker import Faker

from rel_app import app
from one_to_one_many import Employee, Onboarding, Review, db
with app.app_context():
    fake = Faker()
    Employee.query.delete()
    Review.query.delete()
    Onboarding.query.delete()

    uri = Employee(name="Uri Lee", hire_date=datetime.datetime(2024, 5, 17))
    tristan = Employee(name="Tristan Tal", hire_date=datetime.datetime(2020, 1, 30))
    db.session.add_all([uri, tristan])
    db.session.commit()

    uri_2023 = Review(year=2023, summary="Great web developer!", employee_id=1)
    tristan_2021 = Review(year=2021, summary="Good coding skills, often late to work", employee=tristan) # We use the object reference rather than integer after establishing the `relationship` using back_populates
    tristan_2022 = Review(year=2022, summary="Strong coding skills, takes long lunches", employee=tristan)
    tristan_2023 = Review(year=2023, summary="Awesome coding skills, dedicated worker", employee=tristan)
    db.session.add_all([uri_2023, tristan_2021, tristan_2022, tristan_2023])
    db.session.commit()

    uri_onboarding = Onboarding(orientation=datetime.datetime(2023, 3, 27), employee=uri) # Of course, object ref only after establishing relationship.
    tristan_onboarding = Onboarding(orientation=datetime.datetime(2020, 1, 20, 14, 30), forms_complete=True, employee=tristan)

    db.session.add_all([uri_onboarding, tristan_onboarding])
    db.session.commit()
    

