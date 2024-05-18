from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = "Customers"
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(6))
    household_income = db.Column(db.Integer)
    birthdate = db.Column(db.Date)
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String(128), unique=True)


class CarModel(db.Model):
    __tablename__ = "Models"
    model_id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(50), nullable=False)
    model_base_price = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey("Brands.brand_id"))


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


class CarVin(db.Model):
    __tablename__ = "Car_Vins"
    vin = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey("Models.model_id"))
    option_set_id = db.Column(db.Integer, db.ForeignKey("Car_Options.option_set_id"))
    manufactured_date = db.Column(db.Date)
    manufactured_plant_id = db.Column(
        db.Integer, db.ForeignKey("Manufacture_Plant.manufacture_plant_id")
    )


class CarOption(db.Model):
    __tablename__ = "Car_Options"
    option_set_id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey("Models.model_id"))
    engine_id = db.Column(db.Integer)
    transmission_id = db.Column(db.Integer)
    chassis_id = db.Column(db.Integer)
    premium_sound_id = db.Column(db.Integer)
    color = db.Column(db.String(10))
    option_set_price = db.Column(db.Integer)


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


class Dealer(db.Model):
    __tablename__ = "Dealers"
    dealer_id = db.Column(db.Integer, primary_key=True)
    dealer_name = db.Column(db.String(50))
    dealer_address = db.Column(db.String(10))


class DealerBrand(db.Model):
    __tablename__ = "Dealer_Brand"
    dealer_id = db.Column(
        db.Integer, db.ForeignKey("Dealers.dealer_id"), primary_key=True
    )
    brand_id = db.Column(db.Integer, db.ForeignKey("Brands.brand_id"), primary_key=True)


class ManufacturePlant(db.Model):
    __tablename__ = "Manufacture_Plant"
    manufacture_plant_id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(50))
    plant_type = db.Column(db.String(7))
    plant_location = db.Column(db.String(100))
    company_owned = db.Column(db.Boolean)
