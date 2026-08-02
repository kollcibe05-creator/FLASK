from sqlalchemy.orm import validates

class Patient(db.Model):
    __tablename__ = "patients"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_year = db.Column(
        db.CheckConstraint('birth_year < 2023'), 
        nullable=False
    )
    death_year = db.Column(db.Integer)

    insurance_no = db.Column(db.Integer(12))
    phone_no = db.Column(db.String)
    # Constraints defined at table level 
    __table_args__ = (
        db.CheckConstraint('(death_year is NULL) or (death_year >= birth_year)'), 
        db.PrimaryKeyConstraint("id", name="id_pk"), 
        db.UniqueConstraint("unsurance_no", "unique_insurance_no"), 
    ) # if it is a single constraint, don't forget the trailing comma
    # contrived unique constraint
    @validates("insurance_no")
    def unique_insurance(self, key, no):
        if not no:
            raise ValueError("Please provide a number")
        result = Insurance.query.filter_by(number=no).first()
        if result:
            raise ValueError("Unique insurance number only")
        return no

    @validates("phone_no")
    def validate_phone(self, key, value):
        if not value.isdigit():
            raise ValueError("Phone number must be a digit")
        return value
    

class EmailAddress(db.Model):
    __tablename__ = "emailaddresses"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    backup_email = db.Column(db.String)

    # contrived to show constraint
    title = db.Column(db.String)

    @validates('email')
    def validate_email(self, key, address): # arg1: key we want to validate (key's value will be email) arg2: value of what we want to validate
        if '@' not in address:
            raise ValueError("Failed simple email validation")

        return address
    @validates('email', 'backup_email')
    def validate_mai(self, key, value):
        if type(value) not str:
            raise ValueError(f"invalid mail")
        return value
    
    @validates('title')
    def validate_title(self, key, value):
        clickbait_list = ["Secret", "Top", "Trending", "Gossip", "Leak", "Won't believe"]

        if not any(word in title for word in clickbait_list):
            raise ValueError("Title must be clickbait-y!")
        return value