from flask import Blueprint, jsonify
from main import db
from models.store import Store
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.seller_store_schema import store_schema, stores_schema

store = Blueprint('store', __name__, url_prefix="/store")

# Route for users to get all stores back from the database
@store.route('/', methods=["GET"])
@jwt_required()
def get_stores():
    stores_list = Store.query.all()
    result = stores_schema.dump(stores_list)
    return jsonify(result)

@store.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_store(id):
    store = Store.query.get(id)
    result = store_schema.dump(store)
    return jsonify(result)

