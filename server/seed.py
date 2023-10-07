#!/usr/bin/env python3

# Standard library imports
import random
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
        # Seed code goes here!)
        User.query.delete()
        Team.query.delete()
        Player.query.delete()
        Staff.query.delete()
        Game.query.delete()
        db.create_all()

        users = []
        usernames = []
        teams = []

        for i in range(20):
            
            username = fake.first_name()
            while username in usernames:
                username = fake.first_name()
            usernames.append(username)

            user = User(
                username=username,
            )
            user.password_hash = user.username + 'password'

            users.append(user)

        db.session.add_all(users)

        for i in range(4):
            team = Team(
                        name = fake.company(),
                        logo = fake.image_url()
            )
            teams.append(team)
        
        db.session.add_all(users)
        db.session.add_all(teams)
        db.session.commit()

        chosen_user_ids = set()

        players = []

        for team in teams:
            for i in range(10):
                user = rc(users)
                while user.id in chosen_user_ids:
                    user = rc(users)
                chosen_user_ids.add(user.id)
                player = Player(
                                first_name = fake.first_name(),
                                last_name = fake.last_name(),
                                jersey_number = randint(1, 99),
                                user_id = user.id,
                                team_id = team.id
                )
                players.append(player)

        db.session.add_all(players)
        db.session.commit()

        staff_members = []

        for team in teams:
            for i in range(2):
                user = rc(users)
                while user.id in chosen_user_ids:
                    user = rc(users)
                chosen_user_ids.add(user.id)
                staff_member = Staff(
                                    first_name = fake.first_name(),
                                    last_name = fake.last_name(),
                                    user_id = user.id,
                                    team_id = teams.id
                )
                staff_members.append(staff_member)
        
        db.session.add_all(staff_members)
        db.session.commit()

        games = []

        for i in range(5):
            game = Game(
                        name = fake.word(),
                        date = fake.date(),
                        location = fake.address()
            )
            games.append(game)
    
        
        db.session.add_all(games)
        db.session.commit()
    
    print("Done!")