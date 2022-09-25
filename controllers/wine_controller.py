from modulefinder import STORE_GLOBAL
from flask import Blueprint, jsonify, request
from main import db
from models.wine import Wine
from models.store_purchases import StorePurchases
from models.store import Store
from models.user import User
from models.wine_sold import WineSold
from schemas.wine_schema import wine_schema, wines_schema
from schemas.store_purchases_schema import store_purchases_schema, store_purchases_schema_plural
from schemas.wine_sold_schema import wine_sold_schema, wines_sold_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date
from marshmallow.exceptions import ValidationError

wine = Blueprint('wine', __name__, url_prefix="/wine")

#CHECKED Route to get all the wines back from the database
@wine.route("/", methods=["GET"])
@jwt_required()
def get_wines():
    if request.query_string:
        if request.args.get('grape_variety'):
            filtered_wine_list = Wine.query.filter_by(grape_variety=request.args.get('grape_variety'))
            result = wines_schema.dump(filtered_wine_list)
            return jsonify(result)
        else:
            return {"Message": "We don't have any wine in our database that meets that criteria."}, 404

    wine_list = Wine.query.all()
    result = wines_schema.dump(wine_list)
    return jsonify(result)

#CHEKCED Route to get a single wine back based on wine id
@wine.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_wine(id):
    wine = Wine.query.get(id)
    if not wine:
        return {"Sorry": "We can't find that wine in our database. Please try again."}, 404
    result = wine_schema.dump(wine)
    return jsonify(result)

#CHECKED Route to add a new wine to the database. Need to have jwt bearer token and identity="seller" to complete this action.
@wine.route("/", methods=["POST"])
@jwt_required()
def add_wine():
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
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
    return jsonify(wine_schema.dump(wine)), 201

#CHECKED Route to update a wine listing in database based on wine_id. Need to have jwt bearer token and identity="seller" to complete this action.
@wine.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_wine(id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    wine = Wine.query.get(id)
    if not wine:
        return {"Error": "We couldn't find that wine in our database. Please try again"}, 404
    
    wine_fields = wine_schema.load(request.json)

    wine.name = wine_fields["name"]
    wine.grape_variety = wine_fields["grape_variety"]
    wine.vintage = wine_fields["vintage"]
    wine.description = wine_fields["description"]
    wine.price = wine_fields["price"]

    db.session.commit()

    return jsonify(wine_schema.dump(wine)), 201

#CHECKED Route for sellers to delete an individual wine. JWT Token and "seller" identity is required.
@wine.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_wine(id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    
    wine = Wine.query.get(id)
    if not wine:
        return {"Error": "We can't find that wine in our database. Please try again"}, 404

    db.session.delete(wine)
    db.session.commit()

    return {"message": "Wine successfully deleted"}


@wine.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400

     

