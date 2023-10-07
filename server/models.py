from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

# Models go here!

#User table
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(26), nullable=False, unique=True)
    name = db.Column(db.String(), nullable = False)
    _password_hash = db.Column(db.String(128))

    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), unique=True, nullable=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), unique=True, nullable=True)

    player = db.relationship('Player', backref='user', uselist=False)
    staff = db.relationship('Staff', backref='user', uselist=False)


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

    player = db.relationship('Player', backref='team')
    staff = db.relationship('Staff', backref='team')

    def __repr__(self):
        return f'<Team {self.name}, {self.logo}>'
    

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    jersey_number = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))


    def __repr__(self):
        return f'<Player {self.first_name}, {self.last_name}, {self.jersey_number}>'
    

class Staff(db.Model, SerializerMixin):
    __tablename__ = 'staff'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    def __repr__(self):
        return f'<Staff {self.first_name}, {self.last_name}>'
    



    
    

