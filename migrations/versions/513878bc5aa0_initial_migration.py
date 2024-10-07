"""Initial migration

Revision ID: 513878bc5aa0
Revises: 
Create Date: 2024-10-07 23:31:10.738492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '513878bc5aa0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('super_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero_powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hero_id', sa.Integer(), nullable=False),
    sa.Column('power_id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], ),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hero_powers')
    op.drop_table('powers')
    op.drop_table('heroes')
    # ### end Alembic commands ###
