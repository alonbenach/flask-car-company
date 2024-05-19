"""Add Engine model and relationship

Revision ID: 83640bc63a92
Revises: 6bd5c21b86e4
Create Date: 2024-05-19 18:34:20.991873

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "83640bc63a92"
down_revision = "6bd5c21b86e4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Engines",
        sa.Column("engine_id", sa.Integer(), nullable=False),
        sa.Column("engine_type", sa.String(length=50), nullable=True),
        sa.Column("horsepower", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("engine_id"),
    )

    with op.batch_alter_table("Car_Options", schema=None) as batch_op:
        batch_op.add_column(sa.Column("engine_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "fk_car_options_engine_id",  # Name of the foreign key constraint
            "Engines",  # Referenced table
            ["engine_id"],  # Local columns
            ["engine_id"],  # Remote columns
        )

    with op.batch_alter_table("Car_Vins", schema=None) as batch_op:
        batch_op.alter_column(
            "vin",
            existing_type=sa.VARCHAR(length=17),
            type_=sa.Integer(),
            existing_nullable=False,
            autoincrement=True,
        )

    with op.batch_alter_table("Customer_Ownership", schema=None) as batch_op:
        batch_op.alter_column(
            "vin",
            existing_type=sa.VARCHAR(length=17),
            type_=sa.Integer(),
            existing_nullable=False,
        )

    with op.batch_alter_table("Customers", schema=None) as batch_op:
        batch_op.alter_column(
            "first_name", existing_type=sa.VARCHAR(length=50), nullable=True
        )
        batch_op.alter_column(
            "last_name", existing_type=sa.VARCHAR(length=50), nullable=True
        )
        batch_op.alter_column(
            "phone_number",
            existing_type=sa.VARCHAR(length=20),
            type_=sa.String(length=10),
            existing_nullable=True,
        )

    with op.batch_alter_table("Dealers", schema=None) as batch_op:
        batch_op.alter_column(
            "dealer_address",
            existing_type=sa.VARCHAR(length=10),
            type_=sa.String(length=128),
            existing_nullable=True,
        )

    with op.batch_alter_table("Models", schema=None) as batch_op:
        batch_op.alter_column(
            "model_name", existing_type=sa.VARCHAR(length=50), nullable=True
        )
        batch_op.alter_column(
            "model_base_price", existing_type=sa.INTEGER(), nullable=True
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("Models", schema=None) as batch_op:
        batch_op.alter_column(
            "model_base_price", existing_type=sa.INTEGER(), nullable=False
        )
        batch_op.alter_column(
            "model_name", existing_type=sa.VARCHAR(length=50), nullable=False
        )

    with op.batch_alter_table("Dealers", schema=None) as batch_op:
        batch_op.alter_column(
            "dealer_address",
            existing_type=sa.String(length=128),
            type_=sa.VARCHAR(length=10),
            existing_nullable=True,
        )

    with op.batch_alter_table("Customers", schema=None) as batch_op:
        batch_op.alter_column(
            "phone_number",
            existing_type=sa.String(length=10),
            type_=sa.VARCHAR(length=20),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "last_name", existing_type=sa.VARCHAR(length=50), nullable=False
        )
        batch_op.alter_column(
            "first_name", existing_type=sa.VARCHAR(length=50), nullable=False
        )

    with op.batch_alter_table("Customer_Ownership", schema=None) as batch_op:
        batch_op.alter_column(
            "vin",
            existing_type=sa.Integer(),
            type_=sa.VARCHAR(length=17),
            existing_nullable=False,
        )

    with op.batch_alter_table("Car_Vins", schema=None) as batch_op:
        batch_op.alter_column(
            "vin",
            existing_type=sa.Integer(),
            type_=sa.VARCHAR(length=17),
            existing_nullable=False,
            autoincrement=True,
        )

    with op.batch_alter_table("Car_Options", schema=None) as batch_op:
        batch_op.drop_constraint("fk_car_options_engine_id", type_="foreignkey")
        batch_op.drop_column("engine_id")

    op.drop_table("Engines")
    # ### end Alembic commands ###