"""empty message

Revision ID: df639f50094d
Revises: 07d0351ea63c
Create Date: 2022-05-15 16:33:27.138339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df639f50094d'
down_revision = '07d0351ea63c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogs_category_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('blogs_category_id_fkey', 'blogs', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###
