from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()

class ProfileSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    image_url = fields.Str()
    bio = fields.Str()

class TeamSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    logo = fields.Str()

class LeagueSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    logo = fields.Str()
    user = fields.Nested(UserSchema)


