"""empty message

Revision ID: cffd73f27282
Revises: c26d05e0fc2e
Create Date: 2020-06-04 20:28:33.864459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cffd73f27282'
down_revision = 'c26d05e0fc2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
