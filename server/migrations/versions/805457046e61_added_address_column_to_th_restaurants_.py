"""added address column to th restaurants table  

Revision ID: 805457046e61
Revises: 9f5540eb6bcb
Create Date: 2023-09-23 20:00:20.565117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '805457046e61'
down_revision = '9f5540eb6bcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.drop_column('address')

    # ### end Alembic commands ###