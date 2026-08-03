from iam_password_protection_model import User

class Login(Resource):
    def post(self):
        username = request.get_json()['username']
        user = User.query.filter(User.username == username)

        password = request.get_json()['password']

        if user.authenticate(password): # authenticate() defined as instance method
            session['user_id'] = user.id
            return user.to_dict(), 200
        return {'error': 'Invalid username or password'}, 401


# Using Bcrypt
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)

