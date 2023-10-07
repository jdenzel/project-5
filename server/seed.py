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
        # Seed code goes here!

        users = []

        for i in range(48):
            user = User(
                        username = fake.user_name(),
            )
            users.append(user)

        db.session.add_all(users)

        teams = []

        for i in range(4):
            team = Team(
                        name = fake.company(),
                        logo = fake.image_url()
            )
            teams.append(team)
        
        db.session.add_all(teams)

        players = []

        for team in teams:
            for i in range(10):
                player = Player(
                                first_name = fake.first_name(),
                                last_name = fake.last_name(),
                                jersey_number = randint(1, 99),
                                user_id = user.id,
                                team_id = team.id
                )
                players.append(player)

            db.session.add_all(players)

        staff_members = []

        for team in teams:
            for i in range(2):
                staff_member = Staff(
                                    first_name = fake.first_name(),
                                    last_name = fake.last_name(),
                                    user_id = user.id,
                                    team_id = team.id
                )
                staff_members.append(staff_member)
        
        db.session.add_all(staff_members)

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