from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from schemas import UserSchema, ProfileSchema, TeamSchema, LeagueSchema

from config import db, bcrypt

# Models go here!

user_league_association = db.Table('user_league_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('league_id', db.Integer, db.ForeignKey('league.id'))
)


# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    _password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String()) # player or admin



    @hybrid_property
    def password_hash(self):
        raise AttributeError
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f'<User: {self.username}, {self._password_hash}, {self.role}>'
    
    def to_dict(self):
        user_schema = UserSchema()
        return user_schema.dump(self)

# Profile table
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String())
    image_url = db.Column(db.String())
    bio = db.Column(db.String())


    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('profile'), uselist=False)


    def __repr__(self):
        return f'<Profile: {self.first_name}, {self.last_name}, {self.image_url}, {self.bio}>'
    
    def to_dict(self):
        profile_schema = ProfileSchema()
        return profile_schema.dump(self)
    
# Team table
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    logo = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('team'), uselist=False)

    def __repr__(self):
        return f'<Team: {self.name}, {self.logo}>'  
    
    def to_dict(self):
        team_schema = TeamSchema()
        return team_schema.dump(self)

# League table
class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    logo = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('league'))


    def __repr__(self):
        return f'<League: {self.name}, {self.logo}>'
    
    def to_dict(self):
        league_schema = LeagueSchema()
        return league_schema.dump(self)
