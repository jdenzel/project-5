from marshmallow import Schema, fields

class ProfileSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    player = fields.Nested('PlayerSchema')
    staff = fields.Nested('StaffSchema')

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    profile = fields.Nested('ProfileSchema')

class TeamSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    logo = fields.Str()
    players = fields.Nested('PlayerSchema', many=True)
    staff = fields.Nested('StaffSchema', many=True)

class PlayerSchema(Schema):
    id = fields.Int(dump_only=True)
    jersey_number = fields.Int()
    profile = fields.Nested('ProfileSchema')
    team = fields.Nested('TeamSchema')

class StaffSchema(Schema):
    id = fields.Int(dump_only=True)
    profile = fields.Nested('ProfileSchema')
    team = fields.Nested('TeamSchema')

class GameSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    date = fields.Str()
    location = fields.Str()
    players = fields.Nested('PlayerSchema', many=True)

