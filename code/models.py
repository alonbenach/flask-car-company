from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = "Customers"
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(6))
    household_income = db.Column(db.Integer)
    birthdate = db.Column(db.Date)
    phone_number = db.Column(db.String(10))
    email = db.Column(db.String(128))

    # Relationship with CustomerOwnership
    ownerships = db.relationship(
        "CustomerOwnership", back_populates="customer", cascade="all, delete-orphan"
    )


class CarModel(db.Model):
    __tablename__ = "Models"
    model_id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(50))
    model_base_price = db.Column(db.Integer)
    brand_id = db.Column(db.Integer, db.ForeignKey("Brands.brand_id"))

    # Relationship with Brand
    brand = db.relationship("Brand", back_populates="car_models")
    # Relationship with CarVin
    car_vins = db.relationship("CarVin", back_populates="car_model")
    # Relationship with CarOption
    car_options = db.relationship("CarOption", back_populates="car_model")


class CustomerOwnership(db.Model):
    __tablename__ = "Customer_Ownership"
    customer_id = db.Column(
        db.Integer, db.ForeignKey("Customers.customer_id"), primary_key=True
    )
    vin = db.Column(db.Integer, db.ForeignKey("Car_Vins.vin"), primary_key=True)
    purchase_date = db.Column(db.Date)
    purchase_price = db.Column(db.Integer)
    warrantee_expire_date = db.Column(db.Date)
    dealer_id = db.Column(db.Integer, db.ForeignKey("Dealers.dealer_id"))

    # Relationship with Customer
    customer = db.relationship("Customer", back_populates="ownerships")
    # Relationship with CarVin
    car_vin = db.relationship("CarVin", back_populates="ownership")
    # Relationship with Dealer
    dealer = db.relationship("Dealer", back_populates="ownerships")


class CarVin(db.Model):
    __tablename__ = "Car_Vins"
    vin = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey("Models.model_id"))
    option_set_id = db.Column(db.Integer, db.ForeignKey("Car_Options.option_set_id"))
    manufactured_date = db.Column(db.Date)
    manufactured_plant_id = db.Column(
        db.Integer, db.ForeignKey("Manufacture_Plant.manufacture_plant_id")
    )

    # Relationship with CustomerOwnership
    ownership = db.relationship("CustomerOwnership", back_populates="car_vin")
    # Relationship with CarModel
    car_model = db.relationship("CarModel", back_populates="car_vins")
    # Relationship with CarOption
    car_option = db.relationship("CarOption", back_populates="car_vins")
    # Relationship with ManufacturePlant
    manufacture_plant = db.relationship("ManufacturePlant", back_populates="car_vins")


class CarOption(db.Model):
    __tablename__ = "Car_Options"
    option_set_id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey("Models.model_id"))
    engine_id = db.Column(db.Integer, db.ForeignKey("Engines.engine_id"))
    transmission_id = db.Column(db.Integer)
    chassis_id = db.Column(db.Integer)
    premium_sound_id = db.Column(db.Integer)
    color = db.Column(db.String(10))
    option_set_price = db.Column(db.Integer)

    # Relationship with CarVin
    car_vins = db.relationship("CarVin", back_populates="car_option")
    # Relationship with CarModel
    car_model = db.relationship("CarModel", back_populates="car_options")
    # Relationship with Engine
    engine = db.relationship("Engine", back_populates="car_options")


class CarPart(db.Model):
    __tablename__ = "Car_Parts"
    part_id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(100))
    manufacture_plant_id = db.Column(
        db.Integer, db.ForeignKey("Manufacture_Plant.manufacture_plant_id")
    )
    manufacture_start_date = db.Column(db.Date)
    manufacture_end_date = db.Column(db.Date)
    part_recall = db.Column(db.Boolean)


class Brand(db.Model):
    __tablename__ = "Brands"
    brand_id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(50))

    # Relationship with DealerBrand
    dealer_brands = db.relationship("DealerBrand", back_populates="brand")
    # Relationship with CarModel
    car_models = db.relationship("CarModel", back_populates="brand")


class Dealer(db.Model):
    __tablename__ = "Dealers"
    dealer_id = db.Column(db.Integer, primary_key=True)
    dealer_name = db.Column(db.String(50))
    dealer_address = db.Column(db.String(128))

    # Relationship with CustomerOwnership
    ownerships = db.relationship("CustomerOwnership", back_populates="dealer")
    # Relationship with DealerBrand
    dealer_brands = db.relationship("DealerBrand", back_populates="dealer")


class DealerBrand(db.Model):
    __tablename__ = "Dealer_Brand"
    dealer_id = db.Column(
        db.Integer, db.ForeignKey("Dealers.dealer_id"), primary_key=True
    )
    brand_id = db.Column(db.Integer, db.ForeignKey("Brands.brand_id"), primary_key=True)

    # Relationship with Dealer
    dealer = db.relationship("Dealer", back_populates="dealer_brands")
    # Relationship with Brand
    brand = db.relationship("Brand", back_populates="dealer_brands")


class ManufacturePlant(db.Model):
    __tablename__ = "Manufacture_Plant"
    manufacture_plant_id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(50))
    plant_type = db.Column(db.String(7))
    plant_location = db.Column(db.String(100))
    company_owned = db.Column(db.Boolean)

    # Relationship with CarVin
    car_vins = db.relationship("CarVin", back_populates="manufacture_plant")


class Engine(db.Model):
    __tablename__ = "Engines"
    engine_id = db.Column(db.Integer, primary_key=True)
    engine_type = db.Column(db.String(50))
    horsepower = db.Column(db.Integer)

    # Relationship with CarOption
    car_options = db.relationship("CarOption", back_populates="engine")
