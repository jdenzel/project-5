from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from config import db, bcrypt

# Models go here!
# Association table for games and users. Many to many relationship
game_members = db.Table('game_members',
                        db.Column('game_id', db.Integer, ForeignKey('games.id')),
                        db.Column('user_id', db.Integer, ForeignKey('users.id')))

#User table


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

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(26), nullable=False, unique=True)
    _password_hash = db.Column(db.String(128))

    player_id = db.Column(db.Integer, ForeignKey('players.id'), unique=True, nullable=True)
    staff_id = db.Column(db.Integer, ForeignKey('staff.id'), unique=True, nullable=True)

    player = relationship('Player', backref='user', uselist=False, foreign_keys=[player_id])
    staff = relationship('Staff', backref='user', uselist=False, foreign_keys=[staff_id])

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
    
class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    logo = db.Column(db.String())

    player = relationship('Player', backref='team')
    staff = relationship('Staff', backref='team')

    def __repr__(self):
        return f'<Team {self.name}, {self.logo}>'
    

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    jersey_number = db.Column(db.Integer)

    user_id = db.Column(db.Integer, ForeignKey('users.id'), unique=True)
    team_id = db.Column(db.Integer, ForeignKey('teams.id'))


    def __repr__(self):
        return f'<Player {self.first_name}, {self.last_name}, {self.jersey_number}>'
    

class Staff(db.Model, SerializerMixin):
    __tablename__ = 'staff'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    user_id = db.Column(db.Integer, ForeignKey('users.id'), unique=True)
    team_id = db.Column(db.Integer, ForeignKey('teams.id'))

    def __repr__(self):
        return f'<Staff {self.first_name}, {self.last_name}>'
    
class Game(db.Model, SerializerMixin):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    date = db.Column(db.String())
    location = db.Column(db.String())

    member = relationship('User', secondary = 'game_members', backref='game')

    def __repr__(self):
        return f'<Game {self.name}, {self.date}, {self.location}>' 

    



    

