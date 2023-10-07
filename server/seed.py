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

    players = []
    used_user_ids = set()

    for team in teams:
        team_players = 0
        while team_players < 10:
            while True:
                user_id = rc(user_objects).id
                if user_id not in used_user_ids:
                    used_user_ids.add(user_id)
                    break
        player = Player(
            firstname = fake.first_name(),
            lastname = fake.last_name(),
            jersey_number = randint(1, 99),
            user_id = user_id,
            team_id = team.id,
        )

        players.append(player)
        team_players += 1

    team_staff_members = 0
    while team_staff_members < 5:
        while True:
            user_id = rc(user_objects).id
            if user_id not in used_user_ids:
                used_user_ids.add(user_id)
                break
        staff = Staff(
            firstname = fake.first_name(),
            lastname = fake.last_name(),
            user_id = user_id,
            team_id = team.id,
        )
        team_staff_members.append(staff)
        team_staff_members += 1
    
    db.session.add_all(players)
    db.session.add_all(staff)
    db.session.commit()