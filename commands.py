from unicodedata import name
from flask import Blueprint
from main import db
from main import bcrypt
from models.user import User
from models.wine import Wine
from models.vineyard import Vineyard
from models.seller import Seller
from models.store import Store
from models.store_purchases import StorePurchases
from models.wine_sold import WineSold
from datetime import date

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

    vineyard2 = Vineyard(
        name = "Woodland Wines",
        region = "Margaret River"
    )
    db.session.add(vineyard2)

    vineyard3 = Vineyard(
        name = "Gaelic Cemetery",
        region = "Clare Valley"
    )
    db.session.add(vineyard3)
    db.session.commit()

    wine1 = Wine(
        name = "Shaw & Smith Shiraz",
        grape_variety = 'Shiraz',
        vintage = 2020,
        description = 'Firm structured palate, white pepper and spice',
        price = 47.50,
        vineyard = vineyard1
    )
    db.session.add(wine1)

    wine2 = Wine(
        name = "Woodlands Chloe Anne Cabernet Sauvignon",
        grape_variety = "Cabernet Sauvignon",
        vintage = 2017,
        description = "Supple but with latent power, this wine has a very long finish marked by fresh natural acidity.",
        price = 189,
        vineyard = vineyard2
    )
    db.session.add(wine2)

    wine3 = Wine(
        name = "Woodlands Cabernet Merlot 2018",
        grape_variety = "Cabernet Merlot",
        vintage = 2018,
        description = "Soft ripe fruits combine with the array of ripe velvety tannins, finishing with lively acidiy",
        price = 28,
        vineyard = vineyard2
    )
    db.session.add(wine3)

    wine4 = Wine(
        name = "Balhannah Vineyard Shiraz",
        grape_variety = "Shiraz",
        vintage = 2019,
        description = "Juicy, smooth and medium bodied.",
        price = 79,
        vineyard = vineyard1
    )
    db.session.add(wine4)

    wine5 = Wine(
        name = "McAskill Cabernet Malbec",
        grape_variety = "Cabernet Malbec",
        vintage = 2019,
        description = "Medium weight, bright and youthful.",
        price = 50,
        vineyard = vineyard3

    )
    db.session.add(wine5)

    wine6 = Wine(
        name = "Premium Cabernet Malbec",
        grape_variety = "Cabernet Malbec",
        vintage = 2015,
        description = "Warm, firm and structured",
        price = 30,
        vineyard = vineyard3
    )
    db.session.add(wine6)

    user1 = User(
        username = "Jordan",
        email = "jordan.attfield@outlook.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(user1)

    user2 = User(
        username = "Ella",
        email = "ellajune@outlook.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(user2)

    seller1 = Seller(
        email = "admin@blw.com.au",
        username = "george28",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(seller1)

    seller2 = Seller(
        email = "admin@littleripples.com.au",
        username = "AnnaJ",
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        
    )

    db.session.add(seller2)
    db.session.commit()

    store1 = Store(
        name = "Little Ripples Online Wine Sales",
        location = "Brisbane",
        seller = seller2
    )
    db.session.add(store1)

    store2 = Store(
        name = "Corks & Cakes",
        location = "Sydney",
        seller = seller1
    )

    db.session.add(store2)
    db.session.commit()

    storepurchase1 = StorePurchases(
        purchase_date = date.today(),
        user = user1,
        store  = store2,
        wine = wine1

    )
    db.session.add(storepurchase1)
    db.session.commit()

    winesold1 = WineSold(
        store = store2,
        wine = wine1,

    )
    db.session.add(winesold1)
    db.session.commit()

    store3 = Store(
        name = "Naked Wines",
        location = "Melbourne",
        seller = seller2
    
    )
    db.session.add(store3)
    db.session.commit()

    print("Tables seeded")