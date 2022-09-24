from flask import Blueprint, jsonify, request
from main import db
from models.vineyard import Vineyard
from schemas.vineyard_schema import vineyard_schema, vineyards_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError

vineyard = Blueprint('Vineyard', __name__, url_prefix="/vineyards")

#CHECKED Route to get all vineyards back from the database. Need to have JWT token.
@vineyard.route('/', methods=["GET"])
@jwt_required()
def get_vineyards():
    vineyard_list = Vineyard.query.all()
    result = vineyards_schema.dump(vineyard_list)
    return jsonify(result)

#CHECKED Route to get a single vineyard back based on the vineyard id. Need to have JWT token.
@vineyard.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_vineyard(id):
    vineyard = Vineyard.query.get(id)
    if not vineyard:
        return {"Sorry": "We can't find that vineyard in our database. Please try again."}, 404
    result = vineyard_schema.dump(vineyard)
    return jsonify(result)

#CHECKED Route for sellers to add a new vineyard to the database. Need to have jwt token and identity="seller".
@vineyard.route("/", methods=["POST"])
@jwt_required()
def add_vineyard():
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    vineyard_fields = vineyard_schema.load(request.json)
    vineyard = Vineyard(
        name = vineyard_fields["name"],
        region = vineyard_fields["region"]
    )
    db.session.add(vineyard)
    db.session.commit()
    return jsonify(vineyard_schema.dump(vineyard))

#CHECKED Route to update a vineyard. Must have JWT token and identity="seller"
@vineyard.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_vineyard(id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    vineyard = Vineyard.query.get(id)
    if not vineyard:
        return {"Error": "We couldn't find that vineyard in our database. Please try again"}, 404
    
    vineyard_fields = vineyard_schema.load(request.json)

    vineyard.name = vineyard_fields["name"]
    vineyard.region = vineyard_fields["region"]
    
    db.session.commit()

    return jsonify(vineyard_schema.dump(vineyard)), 201


# Route for sellers to delete a vineyard. JWT Token and "seller" identity is required.
@vineyard.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_vineyard(id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    vineyard = Vineyard.query.get(id)
    if not vineyard:
        return {"Error": "We can't find that vineyard in our database. Please try again"}, 404
    db.session.delete(vineyard)
    db.session.commit()

    return {"message": "Vineyard successfully deleted"}

@vineyard.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400