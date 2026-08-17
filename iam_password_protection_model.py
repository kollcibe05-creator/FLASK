from sqlalchemy.ext.hybrid import hybrid_property

def simple_hash(input):
    return sum(bytearray(input, encoding='utf-8'))


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)

    _password_hash = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = self.simple_hash(password)

    def authenticate(self, password):
        return self.simple_hash(password) == self.password_hash # simple hash returns an integer
    # password_hash is 
    @staticmethod
    def simple_hash(input):
        # return sum(bytearray(input, encoding='utf-8'))
        return str(sum(bytearray(input, encoding='utf-8'))) # to avoid mismatch when matching with simple_hash

        


# werkzeug can be used to generate password hashes
from werkzeug.security import generate_password_hash, check_password_hash

@hybrid_property
def password_hash(self):
    return self._password_hash

@password_hash.setter
def password_hash(self, password):
    # Hashes the plain text password securely with salt
        self._password_hash = generate_password_hash(password)

def authenticate(self, password):
    # Safely checks plain text password against stored secure hash
    return check_password_hash(self.password_hash, password)


# Using Bycrypt

from app import bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'

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
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8')
        )

print(str(11))