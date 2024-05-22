from flask import Blueprint, flash, request, render_template, redirect, url_for
from ..models import CarOption, CarModel, CarPart, CarVin, db

caroptions_bp = Blueprint("caroptions", __name__)


@caroptions_bp.route("/car_options", methods=["GET", "POST"])
def car_options():
    if request.method == "POST":
        model_id = request.form.get("model_id")
        engine_id = request.form.get("engine_id")
        transmission_id = request.form.get("transmission_id")
        chassis_id = request.form.get("chassis_id")
        premium_sound_id = request.form.get("premium_sound_id")
        color = request.form.get("color")
        option_set_price = request.form.get("option_set_price")
        car_option = CarOption(
            model_id=model_id,
            engine_id=engine_id,
            transmission_id=transmission_id,
            chassis_id=chassis_id,
            premium_sound_id=premium_sound_id,
            color=color,
            option_set_price=option_set_price,
        )
        db.session.add(car_option)
        db.session.commit()
        return redirect(url_for("caroptions.car_options"))
    car_options = CarOption.query.all()
    return render_template("car_options.html", car_options=car_options)


@caroptions_bp.route("/car_option/new", methods=["GET", "POST"])
def new_car_option():
    if request.method == "POST":
        model_id = request.form.get("model_id")
        engine_id = request.form.get("engine_id")
        transmission_id = request.form.get("transmission_id")
        chassis_id = request.form.get("chassis_id")
        premium_sound_id = request.form.get("premium_sound_id")
        color = request.form.get("color")
        option_set_price = request.form.get("option_set_price")
        car_option = CarOption(
            model_id=model_id,
            engine_id=engine_id,
            transmission_id=transmission_id,
            chassis_id=chassis_id,
            premium_sound_id=premium_sound_id,
            color=color,
            option_set_price=option_set_price,
        )
        db.session.add(car_option)
        db.session.commit()
        return redirect(url_for("caroptions.car_options"))

    car_models = CarModel.query.all()
    car_parts = CarPart.query.all()
    return render_template(
        "carmodel_form.html", car_models=car_models, car_parts=car_parts
    )


@caroptions_bp.route("/car_option/<int:option_set_id>", methods=["GET", "POST"])
def view_car_option(option_set_id):
    car_option = CarOption.query.get_or_404(option_set_id)
    if request.method == "POST":
        car_option.model_id = request.form.get("model_id")
        car_option.engine_id = request.form.get("engine_id")
        car_option.transmission_id = request.form.get("transmission_id")
        car_option.chassis_id = request.form.get("chassis_id")
        car_option.premium_sound_id = request.form.get("premium_sound_id")
        car_option.color = request.form.get("color")
        car_option.option_set_price = request.form.get("option_set_price")
        db.session.commit()
        return redirect(url_for("caroptions.car_options"))

    car_models = CarModel.query.all()
    car_parts = CarPart.query.all()
    return render_template(
        "carmodel_form.html",
        car_option=car_option,
        car_models=car_models,
        car_parts=car_parts,
    )


@caroptions_bp.route("/car_option/<int:option_set_id>/delete", methods=["POST"])
def delete_car_option(option_set_id):
    car_option = CarOption.query.get_or_404(option_set_id)
    try:
        if CarVin.query.filter_by(option_set_id=option_set_id).count() > 0:
            raise ValueError(
                "Car option cannot be deleted because it is associated with a registered car VIN."
            )
        db.session.delete(car_option)
        db.session.commit()
        flash("Car option deleted successfully.", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect(url_for("caroptions.car_options"))
