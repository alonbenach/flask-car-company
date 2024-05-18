from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, ManufacturePlant

manufactureplants_bp = Blueprint("manufactureplants", __name__)


@manufactureplants_bp.route("/manufacture_plants", methods=["GET", "POST"])
def manufacture_plants():
    if request.method == "POST":
        plant_name = request.form.get("plant_name")
        plant_type = request.form.get("plant_type")
        plant_location = request.form.get("plant_location")
        company_owned = request.form.get("company_owned") == "on"
        plant = ManufacturePlant(
            plant_name=plant_name,
            plant_type=plant_type,
            plant_location=plant_location,
            company_owned=company_owned,
        )
        db.session.add(plant)
        db.session.commit()
        return redirect(url_for("manufactureplants.manufacture_plants"))
    manufacture_plants = ManufacturePlant.query.all()
    return render_template(
        "manufacture_plants.html", manufacture_plants=manufacture_plants
    )


@manufactureplants_bp.route("/manufacture_plant/new", methods=["GET", "POST"])
def new_manufacture_plant():
    if request.method == "POST":
        plant_name = request.form.get("plant_name")
        plant_type = request.form.get("plant_type")
        plant_location = request.form.get("plant_location")
        company_owned = request.form.get("company_owned") == "on"
        plant = ManufacturePlant(
            plant_name=plant_name,
            plant_type=plant_type,
            plant_location=plant_location,
            company_owned=company_owned,
        )
        db.session.add(plant)
        db.session.commit()
        return redirect(url_for("manufactureplants.manufacture_plants"))
    return render_template("manufacture_plant_form.html")


@manufactureplants_bp.route(
    "/manufacture_plant/<int:manufacture_plant_id>", methods=["GET", "POST"]
)
def view_manufacture_plant(manufacture_plant_id):
    plant = ManufacturePlant.query.get_or_404(manufacture_plant_id)
    if request.method == "POST":
        plant.plant_name = request.form.get("plant_name")
        plant.plant_type = request.form.get("plant_type")
        plant.plant_location = request.form.get("plant_location")
        plant.company_owned = request.form.get("company_owned") == "on"
        db.session.commit()
        return redirect(url_for("manufactureplants.manufacture_plants"))
    return render_template("manufacture_plant_form.html", plant=plant)


@manufactureplants_bp.route(
    "/manufacture_plant/<int:manufacture_plant_id>/delete", methods=["POST"]
)
def delete_manufacture_plant(manufacture_plant_id):
    plant = ManufacturePlant.query.get_or_404(manufacture_plant_id)
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for("manufactureplants.manufacture_plants"))
