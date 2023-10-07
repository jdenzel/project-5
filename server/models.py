from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    
