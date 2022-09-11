from flask import Blueprint
from main import db
from models.vineyard import Vineyard

vineyard = Blueprint('Vineyard', __name__, url_prefix="/vineyard")

# Route to get all the wine back from the database
@vineyard.route("/", methods=["GET"])
def get_vineyard():
    wine_list = Vineyard.query.all()

    return "Here is a selection of the vineyards that sell our avaialable wines"