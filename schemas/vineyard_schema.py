from main import ma

# Using Marshmallow to serialize vineyard model
class VineyardSchema(ma.Schema):
    class Meta:
        fields = ["vineyard_id", "name", "region"]

vineyard_schema = VineyardSchema()
vineyards_schema = VineyardSchema(many=True)