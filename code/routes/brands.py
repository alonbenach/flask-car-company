from flask import Blueprint, flash, request, render_template, redirect, url_for
from ..models import CarModel, DealerBrand, db, Brand

brands_bp = Blueprint("brands", __name__)


@brands_bp.route("/brands", methods=["GET", "POST"])
def brands():
    if request.method == "POST":
        brand_name = request.form.get("brand_name")
        brand = Brand(brand_name=brand_name)
        db.session.add(brand)
        db.session.commit()
        return redirect(url_for("brands.brands"))
    brands = Brand.query.all()
    return render_template("brands.html", brands=brands)


@brands_bp.route("/brand/new", methods=["GET", "POST"])
def new_brand():
    if request.method == "POST":
        brand_name = request.form.get("brand_name")
        brand = Brand(brand_name=brand_name)
        db.session.add(brand)
        db.session.commit()
        return redirect(url_for("brands.brands"))
    return render_template("brand_form.html")


@brands_bp.route("/brand/<int:brand_id>", methods=["GET", "POST"])
def view_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    if request.method == "POST":
        brand.brand_name = request.form.get("brand_name")
        db.session.commit()
        return redirect(url_for("brands.brands"))
    return render_template("brand_form.html", brand=brand)


@brands_bp.route("/brand/<int:brand_id>/delete", methods=["POST"])
def delete_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    try:
        if (
            CarModel.query.filter_by(brand_id=brand_id).count() > 0
            or DealerBrand.query.filter_by(brand_id=brand_id).count() > 0
        ):
            raise ValueError(
                "Brand is assigned to a car model or dealer brand and cannot be deleted."
            )
        db.session.delete(brand)
        db.session.commit()
        flash("Brand deleted successfully.", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect(url_for("brands.brands"))
