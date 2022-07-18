"""add foreign key to posts table

Revision ID: babdf2fcc853
Revises: 206d804c98b6
Create Date: 2022-07-17 22:53:17.007291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'babdf2fcc853'
down_revision = '206d804c98b6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
