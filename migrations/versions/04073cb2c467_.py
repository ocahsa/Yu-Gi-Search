"""empty message

Revision ID: 04073cb2c467
Revises: 3454780cf770
Create Date: 2022-10-18 20:30:52.848157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04073cb2c467'
down_revision = '3454780cf770'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card_sets', sa.Column('set_price', sa.String(length=255), nullable=True))
    op.add_column('cards', sa.Column('lowest_price', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cards', 'lowest_price')
    op.drop_column('card_sets', 'set_price')
    # ### end Alembic commands ###
