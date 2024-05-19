from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, CarVin, CarModel, CarOption
from datetime import datetime

carvins_bp = Blueprint("carvins", __name__)


@carvins_bp.route("/car_vins", methods=["GET", "POST"])
def car_vins():
    if request.method == "POST":
        vin = request.form.get("vin")
        model_id = request.form.get("model_id")
        option_set_id = request.form.get("option_set_id")
        manufactured_date = datetime.strptime(
            request.form.get("manufactured_date"), "%Y-%m-%d"
        )
        manufactured_plant_id = request.form.get("manufactured_plant_id")
        car_vin = CarVin(
            vin=vin,
            model_id=model_id,
            option_set_id=option_set_id,
            manufactured_date=manufactured_date,
            manufactured_plant_id=manufactured_plant_id,
        )
        db.session.add(car_vin)
        db.session.commit()
        return redirect(url_for("carvins.car_vins"))
    car_vins = CarVin.query.all()
    return render_template("car_vins.html", car_vins=car_vins)


@carvins_bp.route("/car_vin/new", methods=["GET", "POST"])
def new_car_vin():
    car_models = CarModel.query.all()
    car_models_dict = [
        {"model_id": m.model_id, "model_name": m.model_name} for m in car_models
    ]
    car_options = CarOption.query.all()
    car_options_dict = [
        {"option_set_id": o.option_set_id, "option_name": o.option_name}
        for o in car_options
    ]
    if request.method == "POST":
        vin = request.form.get("vin")
        model_id = request.form.get("model_id")
        option_set_id = request.form.get("option_set_id")
        manufactured_date = datetime.strptime(
            request.form.get("manufactured_date"), "%Y-%m-%d"
        )
        manufactured_plant_id = request.form.get("manufactured_plant_id")
        car_vin = CarVin(
            vin=vin,
            model_id=model_id,
            option_set_id=option_set_id,
            manufactured_date=manufactured_date,
            manufactured_plant_id=manufactured_plant_id,
        )
        db.session.add(car_vin)
        db.session.commit()
        return redirect(url_for("carvins.car_vins"))
    return render_template(
        "carvin_form.html", car_models=car_models_dict, car_options=car_options_dict
    )


@carvins_bp.route("/car_vin/<int:vin>", methods=["GET", "POST"])
def view_car_vin(vin):
    car_vin = CarVin.query.get_or_404(vin)
    car_models = CarModel.query.all()
    car_models_dict = [
        {"model_id": m.model_id, "model_name": m.model_name} for m in car_models
    ]
    car_options = CarOption.query.all()
    car_options_dict = [
        {"option_set_id": o.option_set_id, "option_name": o.option_name}
        for o in car_options
    ]
    if request.method == "POST":
        car_vin.model_id = request.form.get("model_id")
        car_vin.option_set_id = request.form.get("option_set_id")
        car_vin.manufactured_date = datetime.strptime(
            request.form.get("manufactured_date"), "%Y-%m-%d"
        )
        car_vin.manufactured_plant_id = request.form.get("manufactured_plant_id")
        db.session.commit()
        return redirect(url_for("carvins.car_vins"))
    return render_template(
        "carvin_form.html",
        car_vin=car_vin,
        car_models=car_models_dict,
        car_options=car_options_dict,
    )


@carvins_bp.route("/car_vin/<int:vin>/delete", methods=["POST"])
def delete_car_vin(vin):
    car_vin = CarVin.query.get_or_404(vin)
    db.session.delete(car_vin)
    db.session.commit()
    return redirect(url_for("carvins.car_vins"))
