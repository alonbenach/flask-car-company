from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../data/Car_Database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import Customer, CarModel


# Routes for CRUD operations
@app.route("/customers", methods=["GET", "POST"])
def handle_customers():
    if request.method == "POST":
        data = request.get_json()
        new_customer = Customer(name=data["name"])
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Customer created"}), 201

    customers = Customer.query.all()
    return jsonify(
        [{"id": customer.id, "name": customer.name} for customer in customers]
    )


@app.route("/customers/<int:id>", methods=["GET", "PUT", "DELETE"])
def handle_customer(id):
    customer = Customer.query.get_or_404(id)

    if request.method == "GET":
        return jsonify({"id": customer.id, "name": customer.name})

    if request.method == "PUT":
        data = request.get_json()
        customer.name = data["name"]
        db.session.commit()
        return jsonify({"message": "Customer updated"})

    if request.method == "DELETE":
        db.session.delete(customer)
        db.session.commit()
        return jsonify({"message": "Customer deleted"})


@app.route("/carmodels", methods=["GET", "POST"])
def handle_carmodels():
    if request.method == "POST":
        data = request.get_json()
        new_car_model = CarModel(name=data["name"])
        db.session.add(new_car_model)
        db.session.commit()
        return jsonify({"message": "Car model created"}), 201

    carmodels = CarModel.query.all()
    return jsonify(
        [{"id": carmodel.id, "name": carmodel.name} for carmodel in carmodels]
    )


@app.route("/carmodels/<int:id>", methods=["GET", "PUT", "DELETE"])
def handle_carmodel(id):
    carmodel = CarModel.query.get_or_404(id)

    if request.method == "GET":
        return jsonify({"id": carmodel.id, "name": carmodel.name})

    if request.method == "PUT":
        data = request.get_json()
        carmodel.name = data["name"]
        db.session.commit()
        return jsonify({"message": "Car model updated"})

    if request.method == "DELETE":
        db.session.delete(carmodel)
        db.session.commit()
        return jsonify({"message": "Car model deleted"})


if __name__ == "__main__":
    app.run(debug=True)
