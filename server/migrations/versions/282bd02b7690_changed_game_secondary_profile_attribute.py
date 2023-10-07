"""Changed game secondary profile attribute

Revision ID: 282bd02b7690
Revises: 347b6cbf1d05
Create Date: 2023-10-07 16:56:03.976754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '282bd02b7690'
down_revision = '347b6cbf1d05'
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
