from main import db

class Vineyard(db.Model):
    __tablename__="vineyard"
    
    vineyard_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    region = db.Column(db.String())