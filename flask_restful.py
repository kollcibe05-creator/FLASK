from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS 
from werkzeug.exceptions import NotFound

app = Flask(__name__)
CORS(app)
api = Api(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found": "The requested resource does not exist", 
        404
    )
    return response

app.register_error_handler(404, handle_not_found)

class Home(Resource):
    def get():
        response_dict = {
            "message": "Welcome Home, Homie"
         }

class Newsletter(Resource):
    def get(self):
       response_dict_list = [n.to_dict() for n in Newsletter.query.all()]

       return make_response(response_dict_list, 200)
    def post():
        new_record = Newsletter(
            title=request.form['title'], 
            body=request.get_json().get("body")
        )
        db.session.add(new_record)
        db.session.commit()

        return make_response(response_dict, 201)

class NewsLetterByID(Resource):
    def get(self, id):
        response_dict = Newsletter.query.filter_by(id=id).first().to_dict()

        return make_response(response_dict, 200)
    
    def patch(self, id):
        newsletter = Newsletter.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(newsletter, attr, request.get_json().attr)
        db.session.add(newsletter)
        db.session.commit()
        newsletter_dict = newsletter.to_dict()
        return make_response(newsletter_dict, 200)
    def delete(self, id):
        record = Newsletter.query.filter_by(id=id).first()
        db.session.delete(record)
        db.session.commit()

        response_dict = {"message": "record deleted successfully"}

        return make_response(response_dict, 204)



api.add_resource(Home, "/")
api.add_resource(Newsletter, '/newsletters')
api.add_resource(NewsLetterByID, '/newsletters/<int:id>')

if __name__ == "__main__":
    app.run(port=555)

