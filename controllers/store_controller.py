from modulefinder import STORE_GLOBAL
from flask import Blueprint, jsonify, request
from main import db
from models.store import Store
from models.user import User
from models.wine import Wine
from models.store_purchases import StorePurchases
from models.wine_sold import WineSold
from schemas.wine_sold_schema import wine_sold_schema, wines_sold_schema
from schemas.store_purchases_schema import store_purchases_schema_plural, store_purchases_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.seller_store_schema import store_schema, stores_schema
from datetime import date
from marshmallow.exceptions import ValidationError

store = Blueprint('store', __name__, url_prefix="/store")

# STORE ROUTES

#CHECKED Route for seller to create a new store. JWT token and seller id  required.
@store.route("/", methods=["POST"])
@jwt_required()
def new_store():
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    store_fields = store_schema.load(request.json)

    store = Store(
        name = store_fields["name"],
        location = store_fields["location"],
        seller_id = store_fields["seller_id"]
    )
   
    db.session.add(store)
    db.session.commit()

    return jsonify(store_schema.dump(store)), 201

#CHECKED Route for users to get all stores back from the database. JWT token required.
@store.route('/', methods=["GET"])
@jwt_required()
def get_stores():
    stores_list = Store.query.all()
    result = stores_schema.dump(stores_list)
    return jsonify(result)


#CHECKED Route for user to return a single store from the database. JWT token required.
@store.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_store(id):
    store = Store.query.get(id)
    if not store:
        return {"Error": "We couldn't find that store in our database. Please try again"}, 404

    result = store_schema.dump(store)
    return jsonify(result)

#CHECKED Route for seller to update store data. JWT token and seller identity required.
@store.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_store(id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    store = Store.query.get(id)
    if not store:
        return {"Error": "We couldn't find that store in our database. Please try again"}, 404

    store_fields = store_schema.load(request.json)

    store.name = store_fields["name"]
    store.location = store_fields["location"]
    store.seller_id = store_fields["seller_id"]

    db.session.commit()

    return jsonify(store_schema.dump(store)), 201

# Route for seller to delete store from database. JWT token and seller identity required
@store.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_store(id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    
    store = Store.query.get(id)
    if not store:
        return {"Error": "We can't find that store in our database. Please try again"}, 404
    
    db.session.delete(store)
    db.session.commit()

    return {"Message": "Store successfully deleted"}

# WINE SOLD ROUTES

#CHECKED Route for seller to view data all wine sold. JWT token and seller identity required (READ).
@store.route('/wine_sold', methods=["GET"])
@jwt_required()
def get_all_wine_sold():
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    wine_sold_list = WineSold.query.all()
    result = wines_sold_schema.dump(wine_sold_list)
    return jsonify(result)

#CHECKED Route for seller to view data on a single wine sold. JWT token and seller identity required (READ).
@store.route('/wine_sold/<int:id>', methods=["GET"])
@jwt_required()
def get_wine_sold(id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    wine_sold = WineSold.query.get(id)
    if not wine_sold:
        return {"Sorry": "We can't find that sales data in our database. Please try again"}, 404

    result = wine_sold_schema.dump(wine_sold)
    return jsonify(result)


 #CHECKED Route for seller to record a wine sale for store. JWT token and seller identity required (CREATE).
@store.route('/<int:wine_id>/wine_sale/<int:store_id>', methods=['POST'])
@jwt_required()
def new_wine_sale(wine_id, store_id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    wine = Wine.query.get(wine_id)
    store = Store.query.get(store_id)

    if not wine:
        return {"error": "We don't have that wine in our database. Please try again."}, 404

    wine_sold = WineSold(
        sale_date = date.today(),
        store = store,
        wine = wine
    )

    db.session.add(wine_sold)
    db.session.commit()

    return jsonify(wine_sold_schema.dump(wine_sold))


#CHECKED Route for seller to update wine sale. JWT token and seller identity required.
@store.route('/wine_sold/<int:wine_sold_id>', methods=['PUT'])
@jwt_required()
def update_wine_sale(wine_sold_id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    wine_sold = WineSold.query.get(wine_sold_id)
    if not store:
        return {"Error": "We couldn't find that transaction in our databse. Please try again."}
    wine_sold_fields = wine_sold_schema.load(request.json)
    sale_date = wine_sold_fields["sale_date"]
    store_id = wine_sold_fields["store_id"]
    wine_id = wine_sold_fields["wine_id"]

    db.session.commit()

    return jsonify(wine_sold_schema.dump(wine_sold)), 201

#CHECKED Route for seller to delete individual wine sale from database. JWT token and seller identity required
@store.route("/wine_sold/<int:wine_sold_id>", methods=["DELETE"])
@jwt_required()
def delete_wine_sold(wine_sold_id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    
    wine_sold = WineSold.query.get(wine_sold_id)
    if not wine_sold:
        return {"Error": "We can't find that sale data in our database. Please try again"}, 404
    
    db.session.delete(wine_sold)
    db.session.commit()

    return {"Message": "Wine sale data successfully deleted"}

# STORE PURCHASE ROUTES

#CHECKED Route for seller to record a new store purchase (CREATE)
@store.route("/purchase", methods=["POST"])
@jwt_required()
def new_store_purchase():
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    store_purchase_fields = store_purchases_schema.load(request.json)

    store_purchase = StorePurchases(
        purchase_date = store_purchase_fields["purchase_date"],
        user_id = store_purchase_fields["user_id"],
        store_id = store_purchase_fields["store_id"],
        wine_id = store_purchase_fields["wine_id"],
    )

    db.session.add(store_purchase)
    db.session.commit()

    return jsonify(store_purchases_schema.dump(store_purchase)), 201


#CHECKED Route to view all purchases. JWT token and seller identity required (READ)
@store.route("/purchases", methods=["GET"])
@jwt_required()
def get_purchases():
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401

    store_purchases_list = StorePurchases.query.all()
    result = store_purchases_schema_plural.dump(store_purchases_list)
    return jsonify(result)


#CHECKED Route for sellers to get individual store purchase transaction data (READ)
@store.route("/purchase/<int:purchase_id>")
@jwt_required()
def get_purchase(purchase_id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401

    store_purchase = StorePurchases.query.get(purchase_id)
    if not store_purchase:
        return {"Error": "We couldn't find that transaction in our database. Please try again."}
    
    result = store_purchases_schema.dump(store_purchase)
    return jsonify(result)

# CHECKED Route for seller to update store purchase data. JWT token and seller identity required (UPDATE)
@store.route("/purchase/<int:store_purchase_id>", methods=["PUT"])
@jwt_required()
def update_store_purchase(store_purchase_id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    store_purchase = StorePurchases.query.get(store_purchase_id)
    if not store_purchase:
        return {"Error": "We couldn't find that purchase data in our database. Please try again"}, 404

    store_purchase_fields = store_purchases_schema.load(request.json)

    store_purchase.purchase_date = store_purchase_fields["purchase_date"]
    store_purchase.user_id = store_purchase_fields["user_id"]
    store_purchase.store_id = store_purchase_fields["store_id"]
    store_purchase.wine_id = store_purchase_fields["wine_id"]

    db.session.commit()

    return jsonify(store_purchases_schema.dump(store_purchase)), 201

# Route for seller to delete individual store purchase data from database. JWT token and seller identity required
@store.route("/purchase/<int:store_purchase_id>", methods=["DELETE"])
@jwt_required()
def delete_store_purchase(store_purchase_id):
    if get_jwt_identity() != "seller":
        return {"Error": "Sorry, you do not have permission to do this"}, 401
    
    store_purchase = StorePurchases.query.get(store_purchase_id)
    if not store_purchase:
        return {"Error": "We can't find that purchase data in our database. Please try again"}, 404
    
    db.session.delete(store_purchase)
    db.session.commit()

    return {"Message": "Store purchase data successfully deleted"}


@store.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400

