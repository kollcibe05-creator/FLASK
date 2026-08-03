from flask import Flask, session, request, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
app.json.compact = False
api = Api(app)
app.secret_key = b'\x8dI)H\xd65\x85\x9d+\xdb\x18$f\xbb\xcdI'

# DRYing login check
@app.before_request
def check_if_logged_in():
    if not session['user_id']:
        return {'error': 'Unathorized'}, 401

# If we wanted to allow users to see a list of documents but restrict other Views(Resources) for login?
@app.before_request
def check_if_logged_in(self):
    if not session['user_id'] \ 
    and request.endpoint != 'document_list': # endpoint is specified when `add_resource()`ing
    return {'error': 'Unathorized'}, 401

class DocumentList(Resource):
    def get():
        documents = [document.to_dict() for document in Document.query.all()]

        return documents, 200

api.add_resource(DocumentList, '/documents', endpoint='document_list')

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401
api.add_resource(CheckSession, '/check_session')
class Login(Resource):
    def post(self):
        user = User.query.filter(User.username == request.get_json()['username']).first()

        session['user_id'] = user.id

        return user.to_dict(), 200

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return {"message": '204: No content'}, 204
api.add_resource(Login, '/login')

# Authorization ~ User must be logged in to access Docs.
class Document(Resource):
    def get(self, id):
        if not session['user_id']: # Logical because as the user logs in we add his id as the session's user_id
            return {'err': 'Unathorized'}, 401
        # The authentication will be repetitive with subsequent CRUD # Sol => app.before_request        
        document = Document.query.filter_by(id=id).first()

        return document.to_dict()

api.add_resource(Document, '/document/<int:id>')
