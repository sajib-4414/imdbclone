"""made some changes

Revision ID: 8e0e6d308685
Revises: 
Create Date: 2023-12-12 03:52:11.310211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e0e6d308685'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.add_column('users', sa.Column('username', sa.String(length=128), nullable=False, server_default='default_username'))
    op.create_unique_constraint(None, 'users', ['username'])
    op.execute("UPDATE users SET username = 'default_username' WHERE username IS NULL")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###