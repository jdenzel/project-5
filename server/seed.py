#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Team, Player, Staff, Game

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        users = []
        usernames = []

        for i in range(110):
        
            username = fake.first_name()
            while username in usernames:
                username = fake.first_name()
            usernames.append(username)

            player_id = randint(1, 100)
            staff_id = randint(1, 10)

            user = User(
                username=username,
                name = fake.name(),
            )

        user.password_hash = user.username + 'password'

        users.append(user)
    db.session.add_all(users)
    db.session.commit()

    teams = []

    for i in range(10):
        team = Team(
            name = fake.company(),
            logo = fake.image_url(),
        )

        teams.append(team)
    
    db.session.add_all(teams)
    db.session.commit()

    user_objects = User.query.all()