"""add verfication columns

Revision ID: 38ce5076a8bd
Revises: 965e8d105dc7
Create Date: 2021-08-10 17:27:50.556410

"""
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
from src.users.db_tables import UserStatus

revision = '38ce5076a8bd'
down_revision = '965e8d105dc7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('status', sa.Text(), nullable=False, default=lambda: UserStatus.CREATED))
    op.add_column('user', sa.Column('verification_id', postgresql.UUID(), nullable=False, default=lambda: uuid.uuid4()))


def downgrade():
    op.drop_column('user', 'verification_id')
    op.drop_column('user', 'status')
