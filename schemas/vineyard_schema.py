from main import ma
from marshmallow import fields

# Using Marshmallow to serialize vineyard model
class VineyardSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["vineyard_id", "name", "region", "wine"]
    wine = fields.List(fields.Nested("VineyardSchema",))

vineyard_schema = VineyardSchema()
vineyards_schema = VineyardSchema(many=True)