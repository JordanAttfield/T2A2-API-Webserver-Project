from main import db

class Store(db.Model):
    __tablename__ = "store"

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String())
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.seller_id"), nullable=False)
