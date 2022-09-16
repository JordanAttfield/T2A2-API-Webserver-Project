from main import ma
from marshmallow.validate import Length

class SellerSchema(ma.Schema):
    class Meta:
        ordered=True
        fields = ("seller_id", "email", "username", "password", "store")

        password = ma.String(validate=Length(min=6))

seller_schema = SellerSchema()
sellers_schema = SellerSchema(many=True)