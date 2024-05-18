from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, CarPart
from datetime import datetime

carparts_bp = Blueprint("carparts", __name__)


@carparts_bp.route("/carparts", methods=["GET", "POST"])
def carparts():
    if request.method == "POST":
        part_name = request.form.get("part_name")
        manufacture_plant_id = request.form.get("manufacture_plant_id")
        manufacture_start_date = datetime.strptime(
            request.form.get("manufacture_start_date"), "%Y-%m-%d"
        ).date()
        manufacture_end_date = datetime.strptime(
            request.form.get("manufacture_end_date"), "%Y-%m-%d"
        ).date()
        part_recall = request.form.get("part_recall") == "on"
        carpart = CarPart(
            part_name=part_name,
            manufacture_plant_id=manufacture_plant_id,
            manufacture_start_date=manufacture_start_date,
            manufacture_end_date=manufacture_end_date,
            part_recall=part_recall,
        )
        db.session.add(carpart)
        db.session.commit()
        return redirect(url_for("carparts.carparts"))
    carparts = CarPart.query.all()
    return render_template("carparts.html", carparts=carparts)


@carparts_bp.route("/carpart/new", methods=["GET", "POST"])
def new_carpart():
    if request.method == "POST":
        part_name = request.form.get("part_name")
        manufacture_plant_id = request.form.get("manufacture_plant_id")
        manufacture_start_date = datetime.strptime(
            request.form.get("manufacture_start_date"), "%Y-%m-%d"
        ).date()
        manufacture_end_date = datetime.strptime(
            request.form.get("manufacture_end_date"), "%Y-%m-%d"
        ).date()
        part_recall = request.form.get("part_recall") == "on"
        carpart = CarPart(
            part_name=part_name,
            manufacture_plant_id=manufacture_plant_id,
            manufacture_start_date=manufacture_start_date,
            manufacture_end_date=manufacture_end_date,
            part_recall=part_recall,
        )
        db.session.add(carpart)
        db.session.commit()
        return redirect(url_for("carparts.carparts"))
    return render_template("carpart_form.html")


@carparts_bp.route("/carpart/<int:part_id>", methods=["GET", "POST"])
def view_carpart(part_id):
    carpart = CarPart.query.get_or_404(part_id)
    if request.method == "POST":
        carpart.part_name = request.form.get("part_name")
        carpart.manufacture_plant_id = request.form.get("manufacture_plant_id")
        carpart.manufacture_start_date = datetime.strptime(
            request.form.get("manufacture_start_date"), "%Y-%m-%d"
        ).date()
        carpart.manufacture_end_date = datetime.strptime(
            request.form.get("manufacture_end_date"), "%Y-%m-%d"
        ).date()
        carpart.part_recall = request.form.get("part_recall") == "on"
        db.session.commit()
        return redirect(url_for("carparts.carparts"))
    return render_template("carpart_form.html", carpart=carpart)


@carparts_bp.route("/carpart/<int:part_id>/delete", methods=["POST"])
def delete_carpart(part_id):
    carpart = CarPart.query.get_or_404(part_id)
    db.session.delete(carpart)
    db.session.commit()
    return redirect(url_for("carparts.carparts"))
