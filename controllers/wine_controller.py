from flask import Blueprint, jsonify, request
from main import db
from models.wine import Wine
from schemas.wine_schema import wine_schema, wines_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

wine = Blueprint('wine', __name__, url_prefix="/wine")

# Route to get all the wines back from the database
@wine.route("/", methods=["GET"])
@jwt_required()
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

# Route to add a new wine to the database. Need to have jwt bearer token and identity="seller" to complete this action.
@wine.route("/", methods=["POST"])
@jwt_required()
def add_wine():
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}
    wine_fields = wine_schema.load(request.json)
    wine = Wine(
        name = wine_fields["name"],
        grape_variety = wine_fields["grape_variety"],
        vintage = wine_fields["vintage"],
        description = wine_fields["description"],
        price = wine_fields["price"],
        vineyard_id = wine_fields["vineyard_id"]
    )

    db.session.add(wine)
    db.session.commit()
    return jsonify(wine_schema.dump(wine))

# Route to update a wine listing in database based on wine_id. Need to have jwt bearer token and identity="seller" to complete this action.
@wine.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_wine(id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}
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
    