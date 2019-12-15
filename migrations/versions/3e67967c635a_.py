"""empty message

Revision ID: 3e67967c635a
Revises: 
Create Date: 2019-12-14 16:45:38.614367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e67967c635a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('OKR_KR',
    sa.Column('_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('progress', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=False),
    sa.Column('startnum', sa.Integer(), nullable=False),
    sa.Column('endnum', sa.Integer(), nullable=False),
    sa.Column('confidencenum', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('avatar_url', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('OKR_O',
    sa.Column('_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('startdate', sa.DateTime(), nullable=True),
    sa.Column('enddate', sa.DateTime(), nullable=True),
    sa.Column('progress', sa.Integer(), nullable=True),
    sa.Column('createuser', sa.Integer(), nullable=False),
    sa.Column('state', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['createuser'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Organization',
    sa.Column('_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Organization')
    op.drop_table('OKR_O')
    op.drop_table('User')
    op.drop_table('OKR_KR')
    # ### end Alembic commands ###
