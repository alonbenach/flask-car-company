"""Initial schema

Revision ID: 63f09dc46107
Revises: 
Create Date: 2024-05-23 01:17:41.807645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63f09dc46107'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Brands',
    sa.Column('brand_id', sa.Integer(), nullable=False),
    sa.Column('brand_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('brand_id')
    )
    op.create_table('Customers',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=6), nullable=True),
    sa.Column('household_income', sa.Integer(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('phone_number', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_table('Dealers',
    sa.Column('dealer_id', sa.Integer(), nullable=False),
    sa.Column('dealer_name', sa.String(length=50), nullable=True),
    sa.Column('dealer_address', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('dealer_id')
    )
    op.create_table('Engines',
    sa.Column('engine_id', sa.Integer(), nullable=False),
    sa.Column('engine_type', sa.String(length=50), nullable=True),
    sa.Column('horsepower', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('engine_id')
    )
    op.create_table('Manufacture_Plant',
    sa.Column('manufacture_plant_id', sa.Integer(), nullable=False),
    sa.Column('plant_name', sa.String(length=50), nullable=True),
    sa.Column('plant_type', sa.String(length=7), nullable=True),
    sa.Column('plant_location', sa.String(length=100), nullable=True),
    sa.Column('company_owned', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('manufacture_plant_id')
    )
    op.create_table('Car_Parts',
    sa.Column('part_id', sa.Integer(), nullable=False),
    sa.Column('part_name', sa.String(length=100), nullable=True),
    sa.Column('manufacture_plant_id', sa.Integer(), nullable=True),
    sa.Column('manufacture_start_date', sa.Date(), nullable=True),
    sa.Column('manufacture_end_date', sa.Date(), nullable=True),
    sa.Column('part_recall', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['manufacture_plant_id'], ['Manufacture_Plant.manufacture_plant_id'], ),
    sa.PrimaryKeyConstraint('part_id')
    )
    op.create_table('Dealer_Brand',
    sa.Column('dealer_id', sa.Integer(), nullable=False),
    sa.Column('brand_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['Brands.brand_id'], ),
    sa.ForeignKeyConstraint(['dealer_id'], ['Dealers.dealer_id'], ),
    sa.PrimaryKeyConstraint('dealer_id', 'brand_id')
    )
    op.create_table('Models',
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('model_name', sa.String(length=50), nullable=True),
    sa.Column('model_base_price', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['Brands.brand_id'], ),
    sa.PrimaryKeyConstraint('model_id')
    )
    op.create_table('Car_Options',
    sa.Column('option_set_id', sa.Integer(), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('engine_id', sa.Integer(), nullable=True),
    sa.Column('transmission_id', sa.Integer(), nullable=True),
    sa.Column('chassis_id', sa.Integer(), nullable=True),
    sa.Column('premium_sound_id', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(length=10), nullable=True),
    sa.Column('option_set_price', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['engine_id'], ['Engines.engine_id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['Models.model_id'], ),
    sa.PrimaryKeyConstraint('option_set_id')
    )
    op.create_table('Car_Vins',
    sa.Column('vin', sa.Integer(), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('option_set_id', sa.Integer(), nullable=True),
    sa.Column('manufactured_date', sa.Date(), nullable=True),
    sa.Column('manufactured_plant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manufactured_plant_id'], ['Manufacture_Plant.manufacture_plant_id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['Models.model_id'], ),
    sa.ForeignKeyConstraint(['option_set_id'], ['Car_Options.option_set_id'], ),
    sa.PrimaryKeyConstraint('vin')
    )
    op.create_table('Customer_Ownership',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('vin', sa.Integer(), nullable=False),
    sa.Column('purchase_date', sa.Date(), nullable=True),
    sa.Column('purchase_price', sa.Integer(), nullable=True),
    sa.Column('warranty_expire_date', sa.Date(), nullable=True),
    sa.Column('dealer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['Customers.customer_id'], ),
    sa.ForeignKeyConstraint(['dealer_id'], ['Dealers.dealer_id'], ),
    sa.ForeignKeyConstraint(['vin'], ['Car_Vins.vin'], ),
    sa.PrimaryKeyConstraint('customer_id', 'vin')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Customer_Ownership')
    op.drop_table('Car_Vins')
    op.drop_table('Car_Options')
    op.drop_table('Models')
    op.drop_table('Dealer_Brand')
    op.drop_table('Car_Parts')
    op.drop_table('Manufacture_Plant')
    op.drop_table('Engines')
    op.drop_table('Dealers')
    op.drop_table('Customers')
    op.drop_table('Brands')
    # ### end Alembic commands ###
