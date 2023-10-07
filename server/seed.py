#!/usr/bin/env python3

# Standard library imports
import random
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Profile, User, Team, Player, Staff, Game

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!)
        Profile.query.delete()
        User.query.delete()
        Team.query.delete()
        Player.query.delete()
        Staff.query.delete()
        Game.query.delete()
        db.create_all()

        users = []
        usernames = []

        for i in range(48):
            username = fake.user_name()
            while username in usernames:
                username = fake.user_name()
            usernames.append(username)

            user = User(
                username=username,
            )
            user.password_hash = user.username + 'password'

            users.append(user)
        db.session.add_all(users)
        db.session.commit()

        profiles = []
        for i in range(48):
            profile = Profile(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )
            profiles.append(profile)

        db.session.add_all(profiles)
        db.session.commit()


        teams = []
        used_profiles = []
        for i in range(4):
            team = Team(
                name=fake.word(),
                logo=fake.image_url(),
            )
            players = []
            for profile in profiles:
                if profile not in used_profiles:
                    player = Player(
                        jersey_number=randint(1, 99),
                        profile_id=profile.id,
                        team_id=team.id
                    )
                    players.append(player)
                    used_profiles.append(profile)
                    if len(players) == 10:
                        break
            
            staff_members = []
            for profile in profiles:
                if profile not in used_profiles:
                    staff = Staff(
                        profile_id=profile.id,
                        team_id=team.id
                    )
                    staff_members.append(staff)
                    used_profiles.append(profile)
                    if len(staff_members) == 2:
                        break

            teams.append(team)
            db.session.add_all(players)
            db.session.add_all(staff_members)
            db.session.add_all(teams)
        db.session.commit()

        games = []

        for i in range(4):
            game = Game(
                name = fake.word(),
                date = fake.date_this_year(),
                location = fake.city()
            )
            games.append(game)
        db.session.add_all(games)
        db.session.commit()

        print(used_profiles)



        print("Done!")