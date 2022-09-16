from main import ma
from marshmallow import fields
from schemas.seller_schema import SellerSchema

class StoreSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["store_id", "name", "location", "seller"]
    seller = fields.Nested(SellerSchema)
    

seller_schema = SellerSchema()
sellers_schema = SellerSchema(many=True)


