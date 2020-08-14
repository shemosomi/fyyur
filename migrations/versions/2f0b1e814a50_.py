"""empty message

Revision ID: 2f0b1e814a50
Revises: cffd73f27282
Create Date: 2020-06-04 22:48:36.460602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f0b1e814a50'
down_revision = 'cffd73f27282'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('address', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'address')
    # ### end Alembic commands ###
