from main import ma
from marshmallow import fields
from schemas.seller_schema import SellerSchema

class StoreSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["store_id", "name", "location", "seller"]
    seller = fields.Nested(SellerSchema)

store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

