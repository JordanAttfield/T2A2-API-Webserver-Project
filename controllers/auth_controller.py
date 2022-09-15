
from datetime import timedelta
from flask import Blueprint, jsonify, request
from main import db
from main import bcrypt
from main import jwt
from flask_jwt_extended import create_access_token
from models.user import User
from schemas.user_schema import user_schema
from models.seller import Seller
from schemas.seller_schema import seller_schema

auth = Blueprint('auth', __name__, url_prefix="/auth")

# Route to register new users
@auth.route("/register", methods=["POST"])
def register_user():
    user_fields = user_schema.load(request.json)
    # Check if user already exists in the database by searching username
    user = User.query.filter_by(username=user_fields["username"]).first()

    if user:
        return {"Error": "That username is already in our database."}

    # Check if user already exists in the databse by searchibng for email address
    user = User.query.filter_by(email=user_fields["email"]).first()
    if user:
        return {"Error": "That email address is already in our database."}

    user = User(
        username = user_fields["username"],
        email = user_fields["email"],
        password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    )
    db.session.add(user)
    db.session.commit()

    # Creating JWT token and setting the identity as user.id
    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))

    return {"username": user.username, "token": token}

# Route to login users
@auth.route("/login", methods=["POST"])
def login_user():
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(username=user_fields["username"]).first()
    if not user:
        return {"Error": "Username is not valid"}

    if not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return {"Error": "Password is not valid"}
    
    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))

    return {"Username": user.username, "token": token}

# Route for sellers to login
@auth.route("/seller/login", methods=["POST"])
def login_seller():
    seller_fields = seller_schema.load(request.json)

    seller = Seller.query.filter_by(username=seller_fields["username"]).first()
    
    if not seller:
        return {"Error": "Username is not valid"}

    if not bcrypt.check_password_hash(seller.password, seller_fields["password"]):
        return {"Error": "Password is not valid"}
    
    token = create_access_token(identity="seller", expires_delta=timedelta(days=1))

    return {"Username": seller.username, "token": token}