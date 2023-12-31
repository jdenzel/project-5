"""first revision

Revision ID: 16922ad298ef
Revises: 6ed9bcae85ca
Create Date: 2023-10-09 16:18:42.482410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16922ad298ef'
down_revision = '6ed9bcae85ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('_password_hash', sa.String(length=128), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('league',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('logo', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_league_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_profile_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('logo', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_team_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_league_association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('league_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['league_id'], ['league.id'], name=op.f('fk_user_league_association_league_id_league')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_league_association_user_id_user'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_league_association')
    op.drop_table('team')
    op.drop_table('profile')
    op.drop_table('league')
    op.drop_table('user')
    # ### end Alembic commands ###
