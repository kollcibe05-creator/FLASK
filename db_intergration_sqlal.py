from flask import Flask, make_response
from flask_migrate import Migrate

from flask_sqlal import db, Pet # Pet for query views

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pets.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json.compact = False   # to display key-value in diff. lines 

migrate = Migrate(app, db)

db.init_app(app)

@app.route("/")
def index():
    response = make_response(
        '<h1>Welcome to the pet directory!</h1>', 
        200
    )
    return response

@app.route("/pets/<int:id>")
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    if pet:
        response_body = f"<p>{pet.name} {pet.species}</p>"
        response_status = 200
    else:
        response_body = f"<p>Pet {id} not found</p>"

        response_status = 404
    response = make_response(response_body, response_status)
    return response

@app.route("/species/<string:species>")
def pet_by_species(species):
    pets = Pet.query.filter_by(species=species).all()
    size = len(pets)
    response_body = f"<h2>There are {size} {species}s</h2>"
    for pet in pets:
        response_body += f"<p>{pet.name}</p>"
    response = make_response(response_body, 200)
    return response

#Returning a json response
@app.route('/demo_json')
def demo_json():
    # pet_json = '{"id": 1, name: "Fido", "species": "Dog"}' # Testing ~ hard-coded json
    pet = Pet.query.first()
    pet_dict = {
        "id": pet.id, 
        "name": pet.name, 
        "species": pet.species
    }
    # return make_response(pet_json, 200) # Also hard-coded
    return make_response(pet_dict, 200)

@app.route("/home")
def home():
    body = {"message": "Welcome to the pet directory!"}
    return make_response(body, 200)

@app.route('/pets/json_form/id/<int:id>')
def pet_by_id_json(id):
    pet = Pet.query.filter_by(id=id).first()
    if pet:
        body = {
            "id": pet.id,
            "name": pet.name, 
            "species": pet.species
        }
        status = 200
    else:
        body = {"messagee": f"Pet {id} not found."}
        status = 404
    return make_response(body, status)
@app.route("/pets/species/<string:species>")
def pets_by_species(species):
    pets = []
    for pet in Pet.query.filter_by(species=species).all():
        pet_dict = {
            "id": pet.id, 
            "name": pet.name
        }
        pets.append(pet_dict)
    body = {
        "count": len(pets), 
        'pets': pets
    }
    return make_response(body, 200)

# to_dict ~ SerializerMixin
@app.route("/pets/id/<int:id>")
def pet_dict_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    if pet:
        body = pet.to_dict()
    else:
        body = {"message": f"Pet {id} not found."}
        status = 404
    return make_response(body, status)
@app.route("species/<string:species>")
def pet_dict_by_species(species):
    pets = []
    for pet in Pet.query.filter_by(species=species):
        pets.append(pet.to_dict())
    body = {
        "count": len(pets),
        "pets": pets   
    }
    return make_response(body, 200)
if __name__ == '__main__':
    app.run(port=5555, debug=True)




