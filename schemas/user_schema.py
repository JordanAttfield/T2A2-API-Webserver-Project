from main import ma
from marshmallow.validate import Length

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "username", "email", "password")

    password = ma.String(validate=Length(min=6))

user_schema = UserSchema()