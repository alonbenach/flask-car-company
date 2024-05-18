from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, CarOption

caroptions_bp = Blueprint("caroptions", __name__)


@caroptions_bp.route("/caroptions", methods=["GET", "POST"])
def caroptions():
    if request.method == "POST":
        model_id = request.form.get("model_id")
        engine_id = request.form.get("engine_id")
        transmission_id = request.form.get("transmission_id")
        chassis_id = request.form.get("chassis_id")
        premium_sound_id = request.form.get("premium_sound_id")
        color = request.form.get("color")
        option_set_price = request.form.get("option_set_price")
        caroption = CarOption(
            model_id=model_id,
            engine_id=engine_id,
            transmission_id=transmission_id,
            chassis_id=chassis_id,
            premium_sound_id=premium_sound_id,
            color=color,
            option_set_price=option_set_price,
        )
        db.session.add(caroption)
        db.session.commit()
        return redirect(url_for("caroptions.caroptions"))
    caroptions = CarOption.query.all()
    return render_template("caroptions.html", caroptions=caroptions)


@caroptions_bp.route("/caroption/new", methods=["GET", "POST"])
def new_caroption():
    if request.method == "POST":
        model_id = request.form.get("model_id")
        engine_id = request.form.get("engine_id")
        transmission_id = request.form.get("transmission_id")
        chassis_id = request.form.get("chassis_id")
        premium_sound_id = request.form.get("premium_sound_id")
        color = request.form.get("color")
        option_set_price = request.form.get("option_set_price")
        caroption = CarOption(
            model_id=model_id,
            engine_id=engine_id,
            transmission_id=transmission_id,
            chassis_id=chassis_id,
            premium_sound_id=premium_sound_id,
            color=color,
            option_set_price=option_set_price,
        )
        db.session.add(caroption)
        db.session.commit()
        return redirect(url_for("caroptions.caroptions"))
    return render_template("caroption_form.html")


@caroptions_bp.route("/caroption/<int:option_set_id>", methods=["GET", "POST"])
def view_caroption(option_set_id):
    caroption = CarOption.query.get_or_404(option_set_id)
    if request.method == "POST":
        caroption.model_id = request.form.get("model_id")
        caroption.engine_id = request.form.get("engine_id")
        caroption.transmission_id = request.form.get("transmission_id")
        caroption.chassis_id = request.form.get("chassis_id")
        caroption.premium_sound_id = request.form.get("premium_sound_id")
        caroption.color = request.form.get("color")
        caroption.option_set_price = request.form.get("option_set_price")
        db.session.commit()
        return redirect(url_for("caroptions.caroptions"))
    return render_template("caroption_form.html", caroption=caroption)


@caroptions_bp.route("/caroption/<int:option_set_id>/delete", methods=["POST"])
def delete_caroption(option_set_id):
    caroption = CarOption.query.get_or_404(option_set_id)
    db.session.delete(caroption)
    db.session.commit()
    return redirect(url_for("caroptions.caroptions"))
