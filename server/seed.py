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
from league_data import league_data
from team_data import team_data

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Deletes existing data from all tables
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


            # Creates profile and player from profile_data and player_data
            for user in users:
                if profile_data:
                    profile_info = profile_data.pop() 
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
                    player_info = player_data.pop() 
                    player = Player(
                        jersey_number=player_info['basketball jersey_number'],
                        user=user
                    )
                    players.append(player)
                    db.session.add(player)

        db.session.commit()


        # Creates league and teams from league_data and team_data
        leagues = []
        teams = []

        for league_info in league_data:
            league = League(
                name = league_info['name'],
                logo = league_info['logo'],
            )
            leagues.append(league)
            db.session.add(league)

        for team_info in team_data:
            team = Team(
                name = team_info['name'],
                logo = team_info['logo'],
                league_id = team_info['league_id']
            )
            teams.append(team)
            db.session.add(team)
        
        db.session.commit()


        # creates association table for players and teams
        players_teams_table = []

        for player in players:
            team = rc(teams)
            print(team)
            players_teams_table.append({
                'player_id': player.id,
                'team_id': team.id
        })

        db.session.execute(players_teams.insert(), players_teams_table)

        db.session.commit()

        print('DONE!')

