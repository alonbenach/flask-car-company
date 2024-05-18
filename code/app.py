from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db
from .routes.customers import customers_bp
from .routes.carmodels import carmodels_bp
from .routes.customer_ownerships import ownerships_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../data/Car_Database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(customers_bp)
app.register_blueprint(carmodels_bp)
app.register_blueprint(ownerships_bp)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run
