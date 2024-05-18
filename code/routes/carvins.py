from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, CarVin
from datetime import datetime

carvins_bp = Blueprint("carvins", __name__)


@carvins_bp.route("/carvins", methods=["GET", "POST"])
def carvins():
    if request.method == "POST":
        vin = request.form.get("vin")
        model_id = request.form.get("model_id")
        option_set_id = request.form.get("option_set_id")
        manufactured_date = datetime.strptime(
            request.form.get("manufactured_date"), "%Y-%m-%d"
        ).date()
        manufactured_plant_id = request.form.get("manufactured_plant_id")
        carvin = CarVin(
            vin=vin,
            model_id=model_id,
            option_set_id=option_set_id,
            manufactured_date=manufactured_date,
            manufactured_plant_id=manufactured_plant_id,
        )
        db.session.add(carvin)
        db.session.commit()
        return redirect(url_for("carvins.carvins"))
    carvins = CarVin.query.all()
    return render_template("carvins.html", carvins=carvins)


@carvins_bp.route("/carvin/new", methods=["GET", "POST"])
def new_carvin():
    if request.method == "POST":
        vin = request.form.get("vin")
        model_id = request.form.get("model_id")
        option_set_id = request.form.get("option_set_id")
        manufactured_date = datetime.strptime(
            request.form.get("manufactured_date"), "%Y-%m-%d"
        ).date()
        manufactured_plant_id = request.form.get("manufactured_plant_id")
        carvin = CarVin(
            vin=vin,
            model_id=model_id,
            option_set_id=option_set_id,
            manufactured_date=manufactured_date,
            manufactured_plant_id=manufactured_plant_id,
        )
        db.session.add(carvin)
        db.session.commit()
        return redirect(url_for("carvins.carvins"))
    return render_template("carvin_form.html")


@carvins_bp.route("/carvin/<string:vin>", methods=["GET", "POST"])
def view_carvin(vin):
    carvin = CarVin.query.get_or_404(vin)
    if request.method == "POST":
        carvin.vin = request.form.get("vin")
        carvin.model_id = request.form.get("model_id")
        carvin.option_set_id = request.form.get("option_set_id")
        carvin.manufactured_date = datetime.strptime(
            request.form.get("manufactured_date"), "%Y-%m-%d"
        ).date()
        carvin.manufactured_plant_id = request.form.get("manufactured_plant_id")
        db.session.commit()
        return redirect(url_for("carvins.carvins"))
    return render_template("carvin_form.html", carvin=carvin)


@carvins_bp.route("/carvin/<string:vin>/delete", methods=["POST"])
def delete_carvin(vin):
    carvin = CarVin.query.get_or_404(vin)
    db.session.delete(carvin)
    db.session.commit()
    return redirect(url_for("carvins.carvins"))
