import email
from main import ma
from marshmallow.validate import Length

class SellerSchema(ma.Schema):
    class Meta:
        ordered=True
        fields = ("seller_id", "email", "username", "password", "store")

        # Validation
        password = ma.String(validate=Length(min=6))
        email = ma.String(required = True)
        username = ma.String(required = True)
        password = ma.String(required = True)

seller_schema = SellerSchema()
sellers_schema = SellerSchema(many=True)