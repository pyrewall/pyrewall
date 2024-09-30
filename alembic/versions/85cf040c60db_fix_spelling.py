"""Fix spelling

Revision ID: 85cf040c60db
Revises: 00e97aafa25f
Create Date: 2024-09-30 03:58:17.943066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '85cf040c60db'
down_revision: Union[str, None] = '00e97aafa25f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('permissions', sa.ARRAY(sa.String()), nullable=False))
    op.drop_column('groups', 'permssions')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('permssions', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False))
    op.drop_column('groups', 'permissions')
    # ### end Alembic commands ###
