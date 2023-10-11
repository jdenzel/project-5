#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports

from models import User, Profile, Player, Team, League


# Views go here!

class Signup(Resource):
    def post(self):
        json_data = request.get_json()
        username = json_data['username']
        password = json_data['password']
        role = json_data['role']

        if username and password:
            new_user = User(
                username = username,
                role = role
            )
            new_user.password_hash = password
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return new_user.to_dict(), 201
        else:
            return {'error': 'Unprocessable entity'}, 422

class CheckSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return user.to_dict()
        else:
            return {'error': 'Unauthorized'}, 401
        

class Login(Resource):
    def post(self):
        username = request.get_json()['username']
        password = request.get_json()['password']

        user = User.query.filter(User.username == username).first()

        if user and user.authenticate(password):
            session['user_id'] = user.id
            return user.to_dict(), 200
        else:
            return {'error': 'Unauthorized'}, 401

class Logout(Resource):
    def delete(self):
        if session.get('user_id'):
            session['user_id'] = None
            return {}, 204
        else:
            return {'error': 'Unauthorized'}, 401
        
# Player profile, can edit Profile info
class UserProfile(Resource):
    def get(self):
        if session.get('user_id'):
            player = Profile.query.filter(Profile.user_id == session['user_id']).first()
            return player.to_dict(), 200
        else:
            return {'error': 'Unauthorized'}, 401
        
    def post(self):
        json_data = request.get_json()
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        image_url = json_data['image_url']
        bio = json_data['bio']

        if session.get('user_id'):
            new_profile = Profile(
                first_name = first_name,
                last_name = last_name,
                image_url = image_url,
                bio = bio,
                user_id = session['user_id']
            )
            db.session.add(new_profile)
            try:
                db.session.commit()
            except Exception:
                return {'error': 'Unprocessable entity'}, 422
            return new_profile.to_dict(), 201
        else:
            return {'error': 'Unauthorized'}, 401

# List of teams
class TeamList(Resource):
    def get(self):
        teams = Team.query.all()
        return [team.to_dict() for team in teams], 200
    
# List of profiles
class ProfileList(Resource):
    def get(self):
        profiles = Profile.query.all()
        return [profile.to_dict() for profile in profiles], 200
    

# List of leagues
class LeagueList(Resource):
    def get(self):
        leagues = League.query.all()
        return [league.to_dict() for league in leagues], 200

    


        
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(UserProfile, '/user_profile', endpoint='user_profile')
api.add_resource(TeamList, '/teams', endpoint='teams')
api.add_resource(ProfileList, '/profiles', endpoint='profiles')
api.add_resource(LeagueList, '/leagues', endpoint='leagues')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

