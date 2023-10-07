#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports

from models import Profile, User, Team, Player, Staff, Game


# Views go here!

class Signup(Resource):
    def post(self):
        json_data = request.get_json()
        username = json_data['username']
        password = json_data['password']
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        player_or_staff = json_data['player_or_staff']

        if username and password:
            new_user = User(
                username=username,
            )
            new_user.password_hash = password
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id

            new_profile = Profile(
                first_name=first_name,
                last_name=last_name,
                player_or_staff=player_or_staff,
            )


            return (
                    new_user.to_dict(), 201,
                    new_profile.to_dict(), 201
            )
        else:
            return {'error': 'Missing data'}, 400
        
api.add_resource(Signup, '/signup', endpoint='signup')
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

