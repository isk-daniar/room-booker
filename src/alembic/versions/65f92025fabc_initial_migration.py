"""initial migration

Revision ID: 65f92025fabc
Revises: 
Create Date: 2024-03-07 11:01:16.668745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65f92025fabc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('hotels',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=True),
        sa.Column('location', sa.String(length=200), nullable=True),
        sa.Column('rating',  sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column("room_number", sa.Integer(), nullable=True),
        sa.Column("floor", sa.Integer(), nullable=True),
        sa.Column("cost", sa.Float(), nullable=True),
        sa.Column("employed", sa.Boolean(), nullable=True),
        sa.Column("number_beds", sa.Integer(), nullable=True),
        sa.Column('hotel_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('hotels')
    op.drop_table('rooms')