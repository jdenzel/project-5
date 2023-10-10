from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from schemas import UserSchema, ProfileSchema, PlayerSchema, TeamSchema, LeagueSchema

from config import db, bcrypt

# Models go here!

players_teams = db.Table('players_teams',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True)
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
    
# Player table
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jersey_number = db.Column(db.Integer())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref =('player'), uselist=False)

    team = db.relationship('Team', secondary=players_teams, backref=db.backref('players', lazy='dynamic'), overlaps='players,team')

    def __repr__(self):
        return f'<Player: {self.jersey_number}, {self.user_id}>'
    
    def to_dict(self):
        player_schema = PlayerSchema()
        return player_schema.dump(self)


# Team table
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    logo = db.Column(db.String())

    league_id = db.Column(db.Integer, db.ForeignKey('league.id'))
    league = db.relationship('League', backref=('team'), uselist=False)

    player = db.relationship('Player', secondary = players_teams, backref=db.backref('teams', lazy='dynamic'), overlaps='players,team')

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

    def __repr__(self):
        return f'<League: {self.name}, {self.logo}>'
    
    def to_dict(self):
        league_schema = LeagueSchema()
        return league_schema.dump(self)
    
