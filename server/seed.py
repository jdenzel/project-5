#!/usr/bin/env python3

# Standard library imports
import random
from random import randint, choice as rc

# Remote library imports
from faker import Faker
from sqlalchemy import text

# Local imports
from app import app
from models import db, User, Profile, Player, Team, League, players_teams
from profile_data import profile_data
from player_data import player_data

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!)
        User.query.delete()
        Profile.query.delete()
        Player.query.delete()
        Team.query.delete()
        League.query.delete()
        players_teams_table = text('DELETE FROM players_teams')
        db.session.execute(players_teams_table)
        db.session.commit()


        # Create Fake users

        users = []
        usernames = []
        players = []
        profiles = []

        for i in range(120):

            username = fake.user_name()
            while username in usernames:
                username = fake.user_name()
            usernames.append(username)

            user = User(
                username = username,
                role = 'player',
            )

            user.password_hash = user.username + 'password'
            db.session.add(user)
            users.append(user)


            random.shuffle(profile_data)
            random.shuffle(player_data)

            for user in users:
                if profile_data:
                    profile_info = profile_data.pop()  # Get the last item from the shuffled list
                    profile = Profile(
                        first_name=profile_info['first_name'],
                        last_name=profile_info['last_name'],
                        image_url=profile_info['image_url'],
                        bio=profile_info['biography'],
                        position=profile_info['basketball_position'],
                        user=user
                    )
                    db.session.add(profile)

                if player_data:
                    player_info = player_data.pop()  # Get the last item from the shuffled list
                    player = Player(
                        jersey_number=player_info['basketball jersey_number'],
                        user=user
                    )
                    players.append(player)
                    db.session.add(player)

        db.session.commit()
                

        #     profile = Profile(
        #         first_name = fake.first_name_male(),
        #         last_name = fake.last_name(),
        #         image_url = fake.image_url(),
        #         bio = fake.paragraph(),
        #         position = rc(['Guard', 'Center', 'Forward']),
        #         user = user
        #     )

        #     profiles.append(profile)
        #     users.append(user)

        #     player = Player(
        #         jersey_number = randint(1, 99),
        #         user = user
        #     )
        #     players.append(player)
        
        # db.session.add_all(users)
        # db.session.add_all(profiles)
        # db.session.add_all(players)



        db.session.commit()


        leagues = []
        teams = []

        for i in range(3):
            league = League(
                name = fake.company(),
                logo = fake.image_url(),
            )
            leagues.append(league)
        db.session.add_all(leagues)

        db.session.commit()

        for league in leagues:
            for i in range(10):
                team = Team(
                    name = fake.company(),
                    logo = fake.image_url(),
                    league_id = league.id
                )
                teams.append(team)
        db.session.add_all(teams)

        db.session.commit()

        players_teams_table = []

        for player in players:
            team = rc(teams)
            players_teams_table.append({
                'player_id': player.id,
                'team_id': team.id
        })

        db.session.execute(players_teams.insert(), players_teams_table)

        db.session.commit()

        print('DONE!')

