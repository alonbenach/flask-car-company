from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, CarPart

carparts_bp = Blueprint("carparts", __name__)


@carparts_bp.route("/car_parts", methods=["GET", "POST"])
def car_parts():
    if request.method == "POST":
        part_name = request.form.get("part_name")
        manufacture_plant_id = request.form.get("manufacture_plant_id")
        manufacture_start_date = request.form.get("manufacture_start_date")
        manufacture_end_date = request.form.get("manufacture_end_date")
        part_recall = request.form.get("part_recall") == "on"
        car_part = CarPart(
            part_name=part_name,
            manufacture_plant_id=manufacture_plant_id,
            manufacture_start_date=manufacture_start_date,
            manufacture_end_date=manufacture_end_date,
            part_recall=part_recall,
        )
        db.session.add(car_part)
        db.session.commit()
        return redirect(url_for("carparts.car_parts"))
    car_parts = CarPart.query.all()
    return render_template("car_parts.html", car_parts=car_parts)


@carparts_bp.route("/car_part/new", methods=["GET", "POST"])
def new_car_part():
    if request.method == "POST":
        part_name = request.form.get("part_name")
        manufacture_plant_id = request.form.get("manufacture_plant_id")
        manufacture_start_date = request.form.get("manufacture_start_date")
        manufacture_end_date = request.form.get("manufacture_end_date")
        part_recall = request.form.get("part_recall") == "on"
        car_part = CarPart(
            part_name=part_name,
            manufacture_plant_id=manufacture_plant_id,
            manufacture_start_date=manufacture_start_date,
            manufacture_end_date=manufacture_end_date,
            part_recall=part_recall,
        )
        db.session.add(car_part)
        db.session.commit()
        return redirect(url_for("carparts.car_parts"))
    return render_template("carpart_form.html")


@carparts_bp.route("/car_part/<int:part_id>", methods=["GET", "POST"])
def view_car_part(part_id):
    car_part = CarPart.query.get_or_404(part_id)
    if request.method == "POST":
        car_part.part_name = request.form.get("part_name")
        car_part.manufacture_plant_id = request.form.get("manufacture_plant_id")
        car_part.manufacture_start_date = request.form.get("manufacture_start_date")
        car_part.manufacture_end_date = request.form.get("manufacture_end_date")
        car_part.part_recall = request.form.get("part_recall") == "on"
        db.session.commit()
        return redirect(url_for("carparts.car_parts"))
    return render_template("carpart_form.html", car_part=car_part)


@carparts_bp.route("/car_part/<int:part_id>/delete", methods=["POST"])
def delete_car_part(part_id):
    car_part = CarPart.query.get_or_404(part_id)
    db.session.delete(car_part)
    db.session.commit()
    return redirect(url_for("carparts.car_parts"))
