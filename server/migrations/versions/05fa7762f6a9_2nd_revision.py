"""2nd revision

Revision ID: 05fa7762f6a9
Revises: f78f0692dc97
Create Date: 2023-10-07 14:36:22.749663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05fa7762f6a9'
down_revision = 'f78f0692dc97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('jersey_number', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_players_team_id_teams')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_players_user_id_users')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_staff_team_id_teams')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_staff_user_id_users')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('logo', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=26), nullable=False),
    sa.Column('_password_hash', sa.String(length=128), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('staff_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], name=op.f('fk_users_player_id_players')),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], name=op.f('fk_users_staff_id_staff')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('player_id'),
    sa.UniqueConstraint('staff_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('game_members',
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_game_members_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_game_members_user_id_users'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_members')
    op.drop_table('users')
    op.drop_table('teams')
    op.drop_table('staff')
    op.drop_table('players')
    op.drop_table('games')
    # ### end Alembic commands ###