"""empty message

Revision ID: 73e67a6db33a
Revises: 3e67967c635a
Create Date: 2019-12-14 16:48:19.134780

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '73e67a6db33a'
down_revision = '3e67967c635a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('OKR_KR', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.drop_column('OKR_KR', '_time')
    op.add_column('OKR_O', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.drop_column('OKR_O', '_time')
    op.add_column('Organization', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.drop_column('Organization', '_time')
    op.add_column('User', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.drop_column('User', '_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('_time', mysql.DATETIME(), nullable=True))
    op.drop_column('User', 'create_time')
    op.add_column('Organization', sa.Column('_time', mysql.DATETIME(), nullable=True))
    op.drop_column('Organization', 'create_time')
    op.add_column('OKR_O', sa.Column('_time', mysql.DATETIME(), nullable=True))
    op.drop_column('OKR_O', 'create_time')
    op.add_column('OKR_KR', sa.Column('_time', mysql.DATETIME(), nullable=True))
    op.drop_column('OKR_KR', 'create_time')
    # ### end Alembic commands ###