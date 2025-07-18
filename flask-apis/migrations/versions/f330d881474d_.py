"""empty message

Revision ID: f330d881474d
Revises: 2faa1daa9ba0
Create Date: 2025-07-12 21:44:46.479689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f330d881474d'
down_revision = '2faa1daa9ba0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('esm_order',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['ems_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('esm_orderitem',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('order_id', sa.String(), nullable=True),
    sa.Column('product_id', sa.String(), nullable=True),
    sa.Column('prices_at_order', sa.Float(), nullable=False),
    sa.Column('order_qty', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['esm_order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['ems_product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('esm_orderitem')
    op.drop_table('esm_order')
    # ### end Alembic commands ###
