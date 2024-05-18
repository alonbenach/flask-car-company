from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, DealerBrand

dealerbrands_bp = Blueprint("dealerbrands", __name__)


@dealerbrands_bp.route("/dealer_brands", methods=["GET", "POST"])
def dealer_brands():
    if request.method == "POST":
        dealer_id = request.form.get("dealer_id")
        brand_id = request.form.get("brand_id")
        dealer_brand = DealerBrand(dealer_id=dealer_id, brand_id=brand_id)
        db.session.add(dealer_brand)
        db.session.commit()
        return redirect(url_for("dealerbrands.dealer_brands"))
    dealer_brands = DealerBrand.query.all()
    return render_template("dealer_brands.html", dealer_brands=dealer_brands)


@dealerbrands_bp.route("/dealer_brand/new", methods=["GET", "POST"])
def new_dealer_brand():
    if request.method == "POST":
        dealer_id = request.form.get("dealer_id")
        brand_id = request.form.get("brand_id")
        dealer_brand = DealerBrand(dealer_id=dealer_id, brand_id=brand_id)
        db.session.add(dealer_brand)
        db.session.commit()
        return redirect(url_for("dealerbrands.dealer_brands"))
    return render_template("dealer_brand_form.html")


@dealerbrands_bp.route(
    "/dealer_brand/<int:dealer_id>/<int:brand_id>", methods=["GET", "POST"]
)
def view_dealer_brand(dealer_id, brand_id):
    dealer_brand = DealerBrand.query.get_or_404((dealer_id, brand_id))
    if request.method == "POST":
        dealer_brand.dealer_id = request.form.get("dealer_id")
        dealer_brand.brand_id = request.form.get("brand_id")
        db.session.commit()
        return redirect(url_for("dealerbrands.dealer_brands"))
    return render_template("dealer_brand_form.html", dealer_brand=dealer_brand)


@dealerbrands_bp.route(
    "/dealer_brand/<int:dealer_id>/<int:brand_id>/delete", methods=["POST"]
)
def delete_dealer_brand(dealer_id, brand_id):
    dealer_brand = DealerBrand.query.get_or_404((dealer_id, brand_id))
    db.session.delete(dealer_brand)
    db.session.commit()
    return redirect(url_for("dealerbrands.dealer_brands"))
