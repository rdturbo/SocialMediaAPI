"""add content column to posts table

Revision ID: 098e53b0768f
Revises: 53d56b213ed7
Create Date: 2022-07-17 22:45:12.447332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '098e53b0768f'
down_revision = '53d56b213ed7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
