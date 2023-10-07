"""Changes secondary of game relationship to profiles

Revision ID: 7776e7a57f61
Revises: 8c13d44da0b6
Create Date: 2023-10-07 16:46:05.736954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7776e7a57f61'
down_revision = '8c13d44da0b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.drop_column('time')

    # ### end Alembic commands ###
