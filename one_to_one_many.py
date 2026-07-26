from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
}) # tells SQLAlchemy: "Whenever a foreign key (fk) is defined, automatically name it using the child table, the child column, and the parent table." => fk_reviews_user_id_users
# SQLite is notoriously picky about modifying existing tables. When altering a table or droping a foreign key later using flask db migrate, Alembic(engine behind Flask-Migrate) needs the exact name of the constraint to drop it.  
# Without explicit constraint name, SQLite won't know what constraint to alter. Flask db migrate will crash or generate broken  scripts when you try to change foreign key relationships.
# Without convention, the cpnstraint name is blank or database-dependent(SQLite might just leave it unnamed). 

# The full dictionary convention:
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"  
} # ck ~ checks 
# One isn't limited to standard placeholders like %(table_name)s SQLAl allows custom esp. to truncate long names so databases like PostgreSQL don't cut them off
def custom_token(constraint, table):
    return table.name.upper()

covention = {
    "my_token": custom_token, 
    "fk": "fk_%(my_token)s_%(column_0_name)s"
}

# if a specific constaint needs a unique or business-specific name, the naming convention dictionary acts as a fallback default. Any name you assign explicitly inside your model will take precedence over the dictionary.  

# email = db.column(db.String, db.UniqueConstraint(name="custom_unique_email_key"))




db = SQLAlchemy(metadata=metadata)

class Employee(db.Model, SerializerMixin):
    ___tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    hire_date = db.Column(db.Date)

    def __repr__(self):
        return f'<Employee {self.id}, {self.name}, {self.hire_date}>'

class Onboarding(db.Model, SerializerMixin):
    ___tablename__ = "onboardings"

    id = db.Column(db.Integer, primary_key=True)
    orientation = db.Column(db.DateTime)
    forms_complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Onboarding {self.id}, {self.orientation}, {self.forms_complete}>"

class Review(db.Model, SerializerMixin):
    ___tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    summary = db.Column(db.String)

    def __repr__(self):
         return f'<Review {self.id}, {self.year}, {self.summary}>'
    


