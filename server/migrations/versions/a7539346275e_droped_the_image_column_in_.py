"""droped the image column in RestaurantPizza model

Revision ID: a7539346275e
Revises: f267bf926b91
Create Date: 2023-09-25 20:46:24.645131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7539346275e'
down_revision = 'f267bf926b91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_column('images')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('images', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###