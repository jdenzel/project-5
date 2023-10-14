#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, jsonify
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
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        image_url = json_data['image_url']
        bio = json_data['bio']
        position = json_data['position']
        jersey_number = json_data['jersey_number']

        if username and password:
            new_user = User(
                username = username,
                role = role
            )
            new_user.password_hash = password
            db.session.add(new_user)

            new_user_profile = Profile(
                first_name = first_name,
                last_name = last_name,
                image_url = image_url,
                bio = bio,
                position = position,
                user = new_user
            )
            db.session.add(new_user_profile)

            if new_user.role == 'player':
                new_user_player = Player(
                    jersey_number = json_data['jersey_number'],
                    user = new_user
                )
                db.session.add(new_user_player)

            db.session.commit()
            session['user_id'] = new_user.id
            return new_user.to_dict(), 201
                
        else:
            return {'error': 'Unprocessable entity'}, 422

class CheckSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            # player = Player.query.filter(Player.user_id == session['user_id']).first()
            return user.to_dict(), 200
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
            profile = Profile.query.filter(Profile.user_id == session['user_id']).first()
            return profile.to_dict(), 200
        else:
            return {'error': 'Unauthorized'}, 401
        
    def patch(self):
        profile = Profile.query.filter(Profile.user_id == session['user_id']).first()
        # player = Player.query.filter(Player.user_id == session['user_id']).first()

        json_data = request.get_json()
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        image_url = json_data['image_url']
        bio = json_data['bio']
        position = json_data['position']
        # jersey_number = json_data['jersey_number']

        if session.get('user_id'):
            if first_name in first_name:
                profile.first_name = first_name
            if last_name in last_name:
                profile.last_name = last_name
            if image_url in image_url:
                profile.image_url = image_url
            if bio in bio:
                profile.bio = bio
            if position in position:
                profile.position = position
            # if jersey_number in jersey_number:
            #     player.jersey_number = jersey_number

            updated_profile = Profile.query.filter(Profile.user_id == session['user_id']).first()
            
            db.session.commit()
        
            return updated_profile.to_dict(), 200
        else:
            return {'error': 'Unauthorized'}, 401
        
    def delete(self):
        if session.get('user_id'):
            profile = Profile.query.filter(Profile.user_id == session['user_id']).first()
            player = Player.query.filter(Player.user_id == session['user_id']).first()
            user = User.query.filter(User.id == session['user_id']).first()
            db.session.delete(profile)
            db.session.delete(player)
            db.session.delete(user)
            db.session.commit()
            session.clear()
            return {'Message': 'Account has been deleted'}, 200
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
api.add_resource(ProfileList, '/players', endpoint='players')
api.add_resource(LeagueList, '/leagues', endpoint='leagues')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

