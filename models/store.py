from main import db
from models.store_purchases import StorePurchases

class Store(db.Model):
    __tablename__ = "store"

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String())
    seller_id = db.Column(db.Integer, db.ForeignKey("sellers.seller_id"), nullable=False)
    store_purchases = db.relationship(
        "StorePurchases",
        backref="store",
        cascade="all, delete"
    )
    wine_sold = db.relationship(
        "WineSold",
        backref="store",
        cascade="all, delete"
    )
