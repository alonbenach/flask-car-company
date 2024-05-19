from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, CarModel, Brand

carmodels_bp = Blueprint("carmodels", __name__)


@carmodels_bp.route("/car_models", methods=["GET", "POST"])
def car_models():
    if request.method == "POST":
        model_name = request.form.get("model_name")
        model_base_price = request.form.get("model_base_price")
        brand_id = request.form.get("brand_id")
        car_model = CarModel(
            model_name=model_name, model_base_price=model_base_price, brand_id=brand_id
        )
        db.session.add(car_model)
        db.session.commit()
        return redirect(url_for("carmodels.car_models"))
    car_models = CarModel.query.all()
    return render_template("car_models.html", car_models=car_models)


@carmodels_bp.route("/car_model/new", methods=["GET", "POST"])
def new_car_model():
    brands = Brand.query.all()
    brands_dict = [{"brand_id": b.brand_id, "brand_name": b.brand_name} for b in brands]
    if request.method == "POST":
        model_name = request.form.get("model_name")
        model_base_price = request.form.get("model_base_price")
        brand_id = request.form.get("brand_id")
        car_model = CarModel(
            model_name=model_name, model_base_price=model_base_price, brand_id=brand_id
        )
        db.session.add(car_model)
        db.session.commit()
        return redirect(url_for("carmodels.car_models"))
    return render_template("carmodel_form.html", brands=brands_dict)


@carmodels_bp.route("/car_model/<int:model_id>", methods=["GET", "POST"])
def view_car_model(model_id):
    car_model = CarModel.query.get_or_404(model_id)
    brands = Brand.query.all()
    brands_dict = [{"brand_id": b.brand_id, "brand_name": b.brand_name} for b in brands]
    if request.method == "POST":
        car_model.model_name = request.form.get("model_name")
        car_model.model_base_price = request.form.get("model_base_price")
        car_model.brand_id = request.form.get("brand_id")
        db.session.commit()
        return redirect(url_for("carmodels.car_models"))
    return render_template(
        "carmodel_form.html", car_model=car_model, brands=brands_dict
    )


@carmodels_bp.route("/car_model/<int:model_id>/delete", methods=["POST"])
def delete_car_model(model_id):
    car_model = CarModel.query.get_or_404(model_id)
    db.session.delete(car_model)
    db.session.commit()
    return redirect(url_for("carmodels.car_models"))
