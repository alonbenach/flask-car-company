"""Initial migration.

Revision ID: 389e422e074d
Revises: 
Create Date: 2024-05-18 14:59:34.927814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '389e422e074d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Car_Vins')
    op.drop_table('Manufacture_Plant')
    op.drop_table('Brands')
    op.drop_table('Customers')
    op.drop_table('Dealers')
    op.drop_table('Dealer_Brand')
    op.drop_table('Car_Options')
    op.drop_table('Car_Parts')
    op.drop_table('Models')
    op.drop_table('Customer_Ownership')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Customer_Ownership',
    sa.Column('customer_id', sa.INTEGER(), nullable=False),
    sa.Column('vin', sa.INTEGER(), nullable=False),
    sa.Column('purchase_date', sa.DATE(), nullable=False),
    sa.Column('purchase_price', sa.INTEGER(), nullable=False),
    sa.Column('warantee_expire_date', sa.DATE(), nullable=True),
    sa.Column('dealer_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['Customers.customer_id'], ),
    sa.ForeignKeyConstraint(['dealer_id'], ['Dealers.dealer_id'], ),
    sa.ForeignKeyConstraint(['vin'], ['Car_Vins.vin'], ),
    sa.PrimaryKeyConstraint('customer_id', 'vin')
    )
    op.create_table('Models',
    sa.Column('model_id', sa.INTEGER(), nullable=True),
    sa.Column('model_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('model_base_price', sa.INTEGER(), nullable=False),
    sa.Column('brand_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['Brands.brand_id'], ),
    sa.PrimaryKeyConstraint('model_id')
    )
    op.create_table('Car_Parts',
    sa.Column('part_id', sa.INTEGER(), nullable=True),
    sa.Column('part_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('manufacture_plant_id', sa.INTEGER(), nullable=False),
    sa.Column('manufacture_start_date', sa.DATE(), nullable=False),
    sa.Column('manufacture_end_date', sa.DATE(), nullable=True),
    sa.Column('part_recall', sa.INTEGER(), server_default=sa.text('0'), nullable=True),
    sa.CheckConstraint('part_recall = 0 or part_recall = 1'),
    sa.ForeignKeyConstraint(['manufacture_plant_id'], ['Manufacture_Plant.manufacture_plant_id'], ),
    sa.PrimaryKeyConstraint('part_id')
    )
    op.create_table('Car_Options',
    sa.Column('option_set_id', sa.INTEGER(), nullable=True),
    sa.Column('model_id', sa.INTEGER(), nullable=True),
    sa.Column('engine_id', sa.INTEGER(), nullable=False),
    sa.Column('transmission_id', sa.INTEGER(), nullable=False),
    sa.Column('chassis_id', sa.INTEGER(), nullable=False),
    sa.Column('premium_sound_id', sa.INTEGER(), nullable=True),
    sa.Column('color', sa.VARCHAR(length=30), nullable=False),
    sa.Column('option_set_price', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['chassis_id'], ['Car_Parts.part_id'], ),
    sa.ForeignKeyConstraint(['engine_id'], ['Car_Parts.part_id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['Models.model_id'], ),
    sa.ForeignKeyConstraint(['premium_sound_id'], ['Car_Parts.part_id'], ),
    sa.ForeignKeyConstraint(['transmission_id'], ['Car_Parts.part_id'], ),
    sa.PrimaryKeyConstraint('option_set_id')
    )
    op.create_table('Dealer_Brand',
    sa.Column('dealer_id', sa.INTEGER(), nullable=False),
    sa.Column('brand_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['Brands.brand_id'], ),
    sa.ForeignKeyConstraint(['dealer_id'], ['Dealers.dealer_id'], ),
    sa.PrimaryKeyConstraint('dealer_id', 'brand_id')
    )
    op.create_table('Dealers',
    sa.Column('dealer_id', sa.INTEGER(), nullable=True),
    sa.Column('dealer_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('dealer_address', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('dealer_id')
    )
    op.create_table('Customers',
    sa.Column('customer_id', sa.INTEGER(), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('gender', sa.NUMERIC(), nullable=True),
    sa.Column('household_income', sa.INTEGER(), nullable=True),
    sa.Column('birthdate', sa.DATE(), nullable=False),
    sa.Column('phone_number', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=128), nullable=True),
    sa.CheckConstraint('gender = "Male" or gender = "Female"'),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_table('Brands',
    sa.Column('brand_id', sa.INTEGER(), nullable=True),
    sa.Column('brand_name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('brand_id')
    )
    op.create_table('Manufacture_Plant',
    sa.Column('manufacture_plant_id', sa.INTEGER(), nullable=True),
    sa.Column('plant_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('plant_type', sa.TEXT(length=7), nullable=True),
    sa.Column('plant_location', sa.VARCHAR(length=100), nullable=True),
    sa.Column('company_owned', sa.INTEGER(), nullable=True),
    sa.CheckConstraint('company_owned=0 or company_owned=1'),
    sa.CheckConstraint('plant_type="Assembly" or plant_type="Parts"'),
    sa.PrimaryKeyConstraint('manufacture_plant_id')
    )
    op.create_table('Car_Vins',
    sa.Column('vin', sa.INTEGER(), nullable=True),
    sa.Column('model_id', sa.INTEGER(), nullable=False),
    sa.Column('option_set_id', sa.INTEGER(), nullable=False),
    sa.Column('manufactured_date', sa.DATE(), nullable=False),
    sa.Column('manufactured_plant_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['manufactured_plant_id'], ['Manufacture_Plant.manufacture_plant_id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['Models.model_id'], ),
    sa.ForeignKeyConstraint(['option_set_id'], ['Car_Options.option_set_id'], ),
    sa.PrimaryKeyConstraint('vin')
    )
    # ### end Alembic commands ###
