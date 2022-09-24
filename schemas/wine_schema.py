from main import ma
from marshmallow import fields
from schemas.vineyard_schema import VineyardSchema

class WineSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["wine_id", "name", "grape_variety", "vintage", "description", "price", "vineyard_id", "vineyard"]
        load_only = ['vineyard_id']
        # Validation
    name = ma.String(required = True)
    vintage = ma.Integer(required = True)
    price = ma.Integer(required = True)
    vineyard = ma.Integer(required = True)


    vineyard = fields.Nested(VineyardSchema, only=("name", "region"))



wine_schema = WineSchema()
wines_schema = WineSchema(many=True)