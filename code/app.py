from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import Brand, CarModel, CarVin, Customer, CustomerOwnership, Dealer, db
from .routes.carmodels import carmodels_bp
from .routes.customers import customers_bp
from .routes.customer_ownerships import ownerships_bp
from .routes.dealer_brands import dealerbrands_bp
from .routes.carvins import carvins_bp
from .routes.caroptions import caroptions_bp
from .routes.carparts import carparts_bp
from .routes.brands import brands_bp
from .routes.dealers import dealers_bp
from .routes.manufacture_plants import manufactureplants_bp


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../data/Car_Database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(customers_bp)
app.register_blueprint(ownerships_bp)
app.register_blueprint(carmodels_bp)
app.register_blueprint(dealerbrands_bp)
app.register_blueprint(carvins_bp)
app.register_blueprint(caroptions_bp)
app.register_blueprint(carparts_bp)
app.register_blueprint(brands_bp)
app.register_blueprint(dealers_bp)
app.register_blueprint(manufactureplants_bp)


@app.route("/")
@app.route("/home")
def home():
    # Fetch data from the database
    customer_ownerships = (
        db.session.query(CustomerOwnership, Customer, CarModel, Brand, CarVin, Dealer)
        .join(Customer, Customer.customer_id == CustomerOwnership.customer_id)
        .join(CarVin, CarVin.vin == CustomerOwnership.vin)
        .join(CarModel, CarModel.model_id == CarVin.model_id)
        .join(Brand, Brand.brand_id == CarModel.brand_id)
        .join(Dealer, Dealer.dealer_id == CustomerOwnership.dealer_id)
        .all()
    )

    return render_template("home.html", customer_ownerships=customer_ownerships)


if __name__ == "__main__":
    app.run(debug=True)
