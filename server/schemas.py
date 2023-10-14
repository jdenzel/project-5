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
    position = fields.Str()


class PlayerSchema(Schema):
    id = fields.Int()
    jersey_number = fields.Int()
    user_id = fields.Nested('UserSchema')
    team_id = fields.Nested('TeamSchema')

class TeamSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    logo = fields.Str()
    league_id = fields.Nested('LeagueSchema')


class LeagueSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    logo = fields.Str()


