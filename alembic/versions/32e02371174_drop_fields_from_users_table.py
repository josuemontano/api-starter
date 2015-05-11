"""Drop fields from users table

Revision ID: 32e02371174
Revises: 2aa08442e7b
Create Date: 2015-05-07 12:15:31.914347

"""

# revision identifiers, used by Alembic.
revision = '32e02371174'
down_revision = '2aa08442e7b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')


def downgrade():
    op.add_column('users', sa.Column('email', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=150), autoincrement=False, nullable=True))
    op.create_unique_constraint('users_email_key', 'users', ['email'])
