from main import ma
from marshmallow.validate import Length

class SellerSchema(ma.Schema):
    class Meta:
        fields = ("seller_id", "shop_name", "email", "username", "password")

        password = ma.String(validate=Length(min=6))

seller_schema = SellerSchema()