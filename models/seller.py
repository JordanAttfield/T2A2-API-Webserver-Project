from main import db

class Seller(db.Model):
    __tablename__ = "sellers"

    seller_id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
