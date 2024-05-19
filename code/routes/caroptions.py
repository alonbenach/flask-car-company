from flask import Blueprint, render_template, request, redirect, url_for
from ..models import CarOption, CarModel, db

caroptions_bp = Blueprint("caroptions", __name__)


@caroptions_bp.route("/car_option/new", methods=["GET", "POST"])
def new_car_option():
    if request.method == "POST":
        model_id = request.form["model_id"]
        engine_id = request.form["engine_id"]
        transmission_id = request.form["transmission_id"]
        chassis_id = request.form["chassis_id"]
        premium_sound_id = request.form["premium_sound_id"]
        color = request.form["color"]
        option_set_price = request.form["option_set_price"]

        new_option = CarOption(
            model_id=model_id,
            engine_id=engine_id,
            transmission_id=transmission_id,
            chassis_id=chassis_id,
            premium_sound_id=premium_sound_id,
            color=color,
            option_set_price=option_set_price,
        )
        db.session.add(new_option)
        db.session.commit()
        return redirect(url_for("caroptions.car_options"))

    car_models = CarModel.query.all()
    return render_template("car_option_form.html", models=car_models)


@caroptions_bp.route("/car_options", methods=["GET"])
def car_options():
    car_options = CarOption.query.all()
    return render_template("car_options.html", car_options=car_options)
