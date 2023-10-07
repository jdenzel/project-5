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

        for i in range(48):
            user = User(
                        username = fake.user_name(),
                        name = fake.name()
            )
            users.append(user)

        teams = []

        for i in range(4):
            team = Team(
                        name = fake.company(),
                        logo = fake.image_url()
            )
            teams.append(team)


    