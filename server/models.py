from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from config import db, bcrypt

# Models go here!
# Association table for games and profukes. Many to many relationship
game_profiles = db.Table('game_profiles',
                        db.Column('game_id', db.Integer, ForeignKey('games.id')),
                        db.Column('profile_id', db.Integer, ForeignKey('profiles.id')))

# Profile table
class Profile(db.Model, SerializerMixin):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    player_id = db.Column(db.Integer, ForeignKey('players.id'), unique=True, nullable=True)
    staff_id = db.Column(db.Integer, ForeignKey('staff.id'), unique=True, nullable=True)

    player = relationship('Player', backref='profile', uselist=False, foreign_keys=[player_id])
    staff = relationship('Staff', backref='profile', uselist=False, foreign_keys=[staff_id])

    def __repr__(self):
        return f'<Profile {self.first_name}, {self.last_name}>'
    

# User table
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(26), nullable=False, unique=True)
    _password_hash = db.Column(db.String(128))

    profile_id = db.Column(db.Integer, ForeignKey('profiles.id'), unique=True)
    profile = relationship('Profile', backref='user', uselist=False)

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
        return f'<User {self.username}, {self.name}, {self._password_hash}>'
    
# Team table
class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    logo = db.Column(db.String())

    player = relationship('Player', backref='team')
    staff = relationship('Staff', backref='team')

    def __repr__(self):
        return f'<Team {self.name}, {self.logo}>'
    
# Player table
class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    jersey_number = db.Column(db.Integer)

    profile_id = db.Column(db.Integer, ForeignKey('profiles.id'))

    def __repr__(self):
        return f'<Player {self.jersey_number}>'
    
# Staff table
class Staff(db.Model, SerializerMixin):
    __tablename__ = 'staff'
    
    id = db.Column(db.Integer, primary_key=True)

    profile_id = db.Column(db.Integer, ForeignKey('profiles.id'))

    def __repr__(self):
        return f'<Staff id: {self.id}'
    
# Game table
class Game(db.Model, SerializerMixin):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    date = db.Column(db.String())
    location = db.Column(db.String())

    profile = relationship('Profile', secondary = 'game_members', backref='game')

    def __repr__(self):
        return f'<Game {self.name}, {self.date}, {self.location}>' 