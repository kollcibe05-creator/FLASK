from flask import make_response, jsonify, Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound 

from models import db, User, Review, Game

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# Works neatly with flask_restful
@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response(
        "Not Found": "The requested resource does not exist", 
        404
    )
    return response

app.register_error_handler(404, handle_not_found)

@app.route('/')
def index():
    return "Hiya"

@app.route("/games")
def games():
    games = []
    for game in Game.query.all():
        game_dict = {
            "title": game.title, 
            "genre": game.genre, 
            "platform": game.platform, 
            "price": game.price
        }
        games.append(game_dict)
    response = make_response(
        jsonify(games),  # jsonify is least effective as it is fussy with even slightly complex Python objects like DateTime
        200,             # Use to_dict() after serializing all the models   
        {"Content-Type": "application/json"}
        )
    return response

@app.route("/games/<int:id>")
def game_by_id(id):
    game = Game.query.filter_by(id=id).first()

    return make_response(game.to_dict(), 200)


@app.route('/games/users/<int:id>')
def game_users_by_id(id):
    game = Game.query.filter(Game.id == id).first()
    # users = []
    # for review in game.reviews:
    #     user = review.user
    #     user_dict = user.to_dict(rules=('-reviews',))
    #     users.append(user_dict)
    users = [review.user.to_dict(rules=('-reviews', ))
            for review in game.reviews
    ]
    return make_response(users, 200)

@app.route('/reviews/<int:id>', methods=['GET', 'DELETE'])
def review_by_id(id):
    review = Review.query.filter_by(id=id).first()

    if request.method == 'GET':
        return make_response(review.to_dict(), 200)
    
    elif request.method == "DELETE": 
        db.sesion.delete(review)
        db.session.commit()

        response_body = {
            "delete_successful": True, 
            "message": "Review deleted"
        }
        response = make_response(
            response_body,
            200
        )
    elif request.method == "PATCH":
        review = Review.query.filter_by(id=id)

        # review.score = request.form.get("score")
        # review.comment = request.form.get("comment")
        # review.game_id=request.form.get("game_id"), 
        # review.user_id=request.form.get("user_id")
        for attr in request.form:
            setattr(review, attr, request.form.get(attr))
        db.session.add(review)
        db.session.commit()

        return make_response(review.to_dict(), 201)


@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == "GET":
        reviews = [review.to_dict() for review in Review.query.all()]

        return make_response(reviews, 200)
    elif request.method == "POST":

        new_review = Review(
            score=request.form.get("score")  # request.form.get() is for html # Use request.get_json()
            comment=request.form.get("comment"), 
            game_id=request.form.get("game_id"), 
            user_id=request.form.get("user_id")
        )

        db.session.add(new_review)

        db.session.commit()

        review_dict = new_review.to_dict()

        return make_response(review_dict, 201)

if __name__ == "__main__":
    app.run(port=5555, debug=True)