from main import ma
from marshmallow.validate import Length

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "username", "email", "password")
    # Validation
    password = ma.String(validate=Length(min=6))
    username = ma.String(required = True)
    email = ma.String(required = True)

user_schema = UserSchema()