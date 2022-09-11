from flask import Blueprint
from main import db
from models.sellers import Seller
from models.wine import Wine
from models.vineyard import Vineyard


db_commands = Blueprint("db", __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    vineyard1 = Vineyard(
        name = 'Shaw and Smith',
        region = 'Adelaide Hills'
    )

    db.session.add(vineyard1)

    wine1 = Wine(
        name = "Shaw & Smith Shiraz",
        grape_variety = 'Shiraz',
        vintage = 2020,
        description = 'Firm structured palate, white pepper and spice',
        price = 47.50
    )
    db.session.add(wine1)
   

    db.session.commit()
    print("Tables seeded")