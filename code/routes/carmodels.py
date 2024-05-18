from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, CarModel

carmodels_bp = Blueprint("carmodels", __name__)


@carmodels_bp.route("/carmodels", methods=["GET", "POST"])
def carmodels():
    if request.method == "POST":
        model_name = request.form.get("model_name")
        model_base_price = request.form.get("model_base_price")
        brand_id = request.form.get("brand_id")
        carmodel = CarModel(
            model_name=model_name, model_base_price=model_base_price, brand_id=brand_id
        )
        db.session.add(carmodel)
        db.session.commit()
        return redirect(url_for("carmodels.carmodels"))
    carmodels = CarModel.query.all()
    return render_template("carmodels.html", carmodels=carmodels)


@carmodels_bp.route("/carmodel/new", methods=["GET", "POST"])
def new_carmodel():
    if request.method == "POST":
        model_name = request.form.get("model_name")
        model_base_price = request.form.get("model_base_price")
        brand_id = request.form.get("brand_id")
        carmodel = CarModel(
            model_name=model_name, model_base_price=model_base_price, brand_id=brand_id
        )
        db.session.add(carmodel)
        db.session.commit()
        return redirect(url_for("carmodels.carmodels"))
    return render_template("carmodel_form.html")


@carmodels_bp.route("/carmodel/<int:model_id>", methods=["GET", "POST"])
def view_carmodel(model_id):
    carmodel = CarModel.query.get_or_404(model_id)
    if request.method == "POST":
        carmodel.model_name = request.form.get("model_name")
        carmodel.model_base_price = request.form.get("model_base_price")
        carmodel.brand_id = request.form.get("brand_id")
        db.session.commit()
        return redirect(url_for("carmodels.carmodels"))
    return render_template("carmodel_form.html", carmodel=carmodel)


@carmodels_bp.route("/carmodel/<int:model_id>/delete", methods=["POST"])
def delete_carmodel(model_id):
    carmodel = CarModel.query.get_or_404(model_id)
    db.session.delete(carmodel)
    db.session.commit()
    return redirect(url_for("carmodels.carmodels"))
