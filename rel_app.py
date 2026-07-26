from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)

from one_to_one_many import db


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///company.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.json.compact= False


migrate = Migrate(app, db)

db.init_app(app)

if __name__ == "__main__":
    app.run(port=5555, debug=True)