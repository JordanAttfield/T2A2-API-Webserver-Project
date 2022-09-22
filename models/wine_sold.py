from main import db

class WineSold(db.Model):
    __tablename__ = "wine_sold"

    wine_sold_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("store.store_id"), nullable=False)
    wine_id = db.Column(db.Integer, db.ForeignKey("wine.wine_id"), nullable=False)