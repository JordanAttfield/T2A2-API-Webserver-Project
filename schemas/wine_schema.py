from main import ma

class WineSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["wine_id", "name", "grape_variety", "vintage", "description", "price"]

wine_schema = WineSchema()
wines_schema = WineSchema(many=True)