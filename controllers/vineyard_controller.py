from flask import Blueprint, jsonify, request
from main import db
from models.vineyard import Vineyard
from schemas.vineyard_schema import vineyard_schema, vineyards_schema

vineyard = Blueprint('Vineyard', __name__, url_prefix="/vineyards")

# Route to get all the wines back from the database
@vineyard.route("/", methods=["GET"])
def get_wines():
    vineyards_list = Vineyard.query.all()
    result = vineyards_schema.dump(vineyards_list)
    return jsonify(result)

# Route to get a single vineyard back based on the vineyard id
@vineyard.route("/<int:id>", methods=["GET"])
def get_vineyard(id):
    vineyard = Vineyard.query.get(id)
    if not vineyard:
        return{"Sorry": "We can't find that vineyard in our database. Please try again."}
    result = vineyard_schema.dump(vineyard)
    return jsonify(result)

# Route for sellers to add a new vineyard to the database
@vineyard.route("/", methods=["POST"])
def add_vineyard():
    vineyard_fields = vineyard_schema.load(request.json)
    vineyard = Vineyard(
        name = vineyard_fields["name"],
        region = vineyard_fields["region"]
    )
    db.session.add(vineyard)
    db.session.commit()
    return jsonify(vineyard_schema.dump(vineyard))

# Route for sellers to delete a vineyard
@vineyard.route("/<int:id>", methods=["DELETE"])
def delete_vineyard(id):
    vineyard = Vineyard.query.get(id)
    if not vineyard:
        return{"Error": "We can't find that vineyard in our database. Please try again"}
    db.session.delete(vineyard)
    db.session.commit()

    return {"message": "Vineyard successfully deleted"}