from main import ma

class WineSoldSchema(ma.Schema):
    class Meta:
        ordered=True
        fields = ["wine_sold_id", "sale_date", "store_id", "wine_id"]

wine_sold_schema = WineSoldSchema()
wines_sold_schema = WineSoldSchema(many=True)