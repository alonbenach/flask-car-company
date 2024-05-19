"""Change vin to String in Car_Vins

Revision ID: 6bd5c21b86e4
Revises: 3ecc128f7c84
Create Date: 2024-05-19 15:15:37.888135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bd5c21b86e4'
down_revision = '3ecc128f7c84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Car_Vins', schema=None) as batch_op:
        batch_op.alter_column('vin',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=17),
               existing_nullable=False)

    with op.batch_alter_table('Customer_Ownership', schema=None) as batch_op:
        batch_op.alter_column('vin',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=17),
               existing_nullable=False)

    with op.batch_alter_table('Customers', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Customers', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.String(length=20),
               type_=sa.INTEGER(),
               existing_nullable=True)

    with op.batch_alter_table('Customer_Ownership', schema=None) as batch_op:
        batch_op.alter_column('vin',
               existing_type=sa.String(length=17),
               type_=sa.INTEGER(),
               existing_nullable=False)

    with op.batch_alter_table('Car_Vins', schema=None) as batch_op:
        batch_op.alter_column('vin',
               existing_type=sa.String(length=17),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###