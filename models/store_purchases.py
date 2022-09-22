from main import db

class StorePurchases(db.Model):
    __tablename__ = "store_purchases"

    store_purchases_id = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.Date())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("store.store_id"), nullable=False)
    wine_id = db.Column(db.Integer, db.ForeignKey("wine.wine_id"), nullable=False)
