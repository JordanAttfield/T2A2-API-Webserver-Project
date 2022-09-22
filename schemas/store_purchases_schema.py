from main import ma
from marshmallow import fields

class StorePurchases(ma.Schema):
    class Meta:
        ordered=True
        fields = ["store_purchases_id", "purchase_date" "user_id", "store_id", "wine_id"]

store_purchases_schema = StorePurchases()
store_purchases_schema_plural = StorePurchases(many=True)