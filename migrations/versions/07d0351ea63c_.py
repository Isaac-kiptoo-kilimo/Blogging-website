"""empty message

Revision ID: 07d0351ea63c
Revises: 548b8dcac0fa
Create Date: 2022-05-15 15:51:41.451142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d0351ea63c'
down_revision = '548b8dcac0fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'bio',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'bio',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###