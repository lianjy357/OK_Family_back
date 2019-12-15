"""empty message

Revision ID: 8e068f29d381
Revises: 73e67a6db33a
Create Date: 2019-12-14 16:56:56.995779

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8e068f29d381'
down_revision = '73e67a6db33a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('OKR_KR', sa.Column('krtype', sa.String(length=64), nullable=False))
    op.drop_column('OKR_KR', 'type')
    op.add_column('OKR_O', sa.Column('otype', sa.Integer(), nullable=False))
    op.drop_column('OKR_O', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('OKR_O', sa.Column('type', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('OKR_O', 'otype')
    op.add_column('OKR_KR', sa.Column('type', mysql.VARCHAR(length=64), nullable=False))
    op.drop_column('OKR_KR', 'krtype')
    # ### end Alembic commands ###
