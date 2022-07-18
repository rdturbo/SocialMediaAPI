"""add user table

Revision ID: 206d804c98b6
Revises: 098e53b0768f
Create Date: 2022-07-17 22:49:28.174823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '206d804c98b6'
down_revision = '098e53b0768f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
