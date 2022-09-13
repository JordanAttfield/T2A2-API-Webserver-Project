from flask import Blueprint, jsonify, request
from main import db
from models.wine import Wine
from schemas.wine_schema import wine_schema, wines_schema

wine = Blueprint('wine', __name__, url_prefix="/wine")

# Route to get all the wines back from the database
@wine.route("/", methods=["GET"])
def get_wines():
    wine_list = Wine.query.all()
    result = wines_schema.dump(wine_list)
    return jsonify(result)

# Route to get a single wine back based on wine id
@wine.route("/<int:id>", methods=["GET"])
def get_wine(id):
    wine = Wine.query.get(id)
    result = wine_schema.dump(wine)
    return jsonify(result)

# Route to add a new wine to the database
@wine.route("/", methods=["POST"])
def add_wine():
    wine_fields = wine_schema.load(request.json)
    wine = Wine(
        name = wine_fields["name"],
        grape_variety = wine_fields["grape_variety"],
        vintage = wine_fields["vintage"],
        description = wine_fields["description"],
        price = wine_fields["price"]
    )

    db.session.add(wine)
    db.session.commit()
    return jsonify(wine_schema.dump(wine))

# Route to update a wine listing in database based on wine_id
@wine.route("/<int:id>", methods=["PUT"])
def update_wine(id):
    wine = Wine.query.get(id)
    if not wine:
        return {"Error": "We couldn't find that wine in our database. Please try again"}
    
    wine_fields = wine_schema.load(request.json)

    wine.name = wine_fields["name"]
    wine.grape_variety = wine_fields["grape_variety"]
    wine.vintage = wine_fields["vintage"]
    wine.description = wine_fields["description"]
    wine.price = wine_fields["price"]

    db.session.commit()

    return jsonify(wine_schema.dump(wine))
    