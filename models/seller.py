from main import db
from models.store import Store

class Seller(db.Model):
    __tablename__ = "sellers"

    seller_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    store = db.relationship(
        "Store",
        backref = "seller",
        cascade="all, delete"
    )
    


    
   
    