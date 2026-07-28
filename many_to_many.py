from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"  
})

db = SQLAlchemy(metadata=metadata)

employee_meetings = db.Table(
    "employee_meetings", 
    metadata, 
    db.Column("employee_id", db.Integer, db.ForeignKey("employees.id"), primary_key=True)
    db.Column("meeting_id", db.Integer, db.ForeignKey("meetings.id"), primary_key=True)
)

class Employee(db.Model, SerializerMixin):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    hire_date=db.Column(db.Date)

    meetings = db.relationship(
        "Meeting", 
        secondary=employee_meetings, 
        back_populates="employees"
    )

class Meeting(db.Model, SerializerMixin):
    __tablename__ = "meetings"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    scheduled_time = db.Column(db.DateTime)
    location = db.Column(db.String)

    employees = db.relationship(
        "Employee", 
        secondary=employee_meetings, 
        back_populates="meetings"
    )

