from main import db

class Wine(db.Model):
    __tablename__="wine"

    wine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    category = db.Column(db.String())
    vintage = db.Column(db.Integer)
    description = db.Column(db.String())
    price = db.Column(db.Integer)