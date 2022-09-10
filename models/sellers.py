from main import db

class Seller(db.Model):
    __tablename__="sellers"
    seller_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())