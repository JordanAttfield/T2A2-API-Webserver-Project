from main import db
from models.store_purchases import StorePurchases

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    store_purchases = db.relationship(
        "StorePurchases",
        backref="user",
        cascade="all, delete"
    )
    