from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

from marshmallow_model import db, Newsletter

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

ma = Marshmallow(app)

class NewsletterSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Newsletter
        load_instance = True

    title = ma.auto_field()
    published_at = ma.auto_field()

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "newsletterbyid", 
                values=dict(id='<id>')
            ),
            "collection": ma.URLFor("newsletters"),  # Having both 'newsletters' and 'newsletterbyid' endpoints, both Resources must be defined and referenced for the effectiveness of the config.
        }
    )

newsletter_schema = NewsletterSchema()
newsletters_schema = NewsletterSchema(many=True)


class index(Resource):
    def get(self):
        response_dict = {
            "index": "Welcome to the Newsletter RESTful API"
        }
        return make_response(
            response_dict, 
            200
        )
api.add_resource(index, "/")
class Newsletters(Resource):
    def get(self):
        newsletters = Newsletter.query.all()

        return make_response(
            newsletters_schema.dump(newsletters), 
            200
        )

api.add_resource(Newsletters, '/newsletters')

class NewsletterByID(Resource):
    def get(self, id):
        newsletter = Newsletter.query.filter_by(id=id).first()

        response = make_response(
            newsletter_schema.dump(newsletter), 
            200
        )

        return response

api.add_resource(NewsletterByID, '/newsletters/<int:id>', endpoint="newsletterbyid" ) 
# endpoint and URL serve different purposes. 
# URL path is what the user/client types into their browser or HTTP client to reach resource
# Endpoint name is the internal name Flask gives to that route.  
# Flask uses this internal identifier for URL building (`url_for()`) or ma.URLFor()
# Passing only the URL prompts Flask-RESTful to automatically generate a default endpoint name by lowercasing the class name
# Passing both guarantees that refactoring class names won't break the schema links
# If you have two Resource classes with the same URLs, each must have a unique endpoint name
# Passing only an endpoint doesn't work in Flask_RESTful because a web server cannot route an incoming HTTP request without a URL path patterns to match against. Flask needs to know what URL path triggers the code

if __name__ == "__main__":
    app.run(port=5555, debug=True)