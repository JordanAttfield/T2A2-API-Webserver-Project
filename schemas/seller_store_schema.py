from main import ma
from marshmallow import fields
from schemas.seller_schema import SellerSchema
from schemas.wine_schema import WineSchema

class StoreSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["store_id", "name", "location", "seller_id"]
    
    name = ma.String(required=True)
    location = ma.String(required=True)
   


    seller = fields.List(fields.Nested("SellerSchema"))

store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

