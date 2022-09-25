from main import db
from models.store_purchases import StorePurchases

class Wine(db.Model):
    __tablename__="wine"

    wine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    grape_variety = db.Column(db.String())
    vintage = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String())
    price = db.Column(db.Integer, nullable=False)
    vineyard_id = db.Column(db.Integer, db.ForeignKey("vineyard.vineyard_id"))
    store_purchases = db.relationship(
        "StorePurchases",
        backref="wine",
        cascade="all, delete"
    )
    wine_sold = db.relationship(
        "WineSold",
        backref="wine",
        cascade="all, delete"
    )
    
  
