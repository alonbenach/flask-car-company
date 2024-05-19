from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, CustomerOwnership, Customer, CarVin

ownerships_bp = Blueprint("ownerships", __name__)


@ownerships_bp.route("/customer_ownerships", methods=["GET", "POST"])
def customer_ownerships():
    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        vin = request.form.get("vin")
        purchase_date = request.form.get("purchase_date")
        purchase_price = request.form.get("purchase_price")
        warrantee_expire_date = request.form.get("warrantee_expire_date")
        dealer_id = request.form.get("dealer_id")
        ownership = CustomerOwnership(
            customer_id=customer_id,
            vin=vin,
            purchase_date=purchase_date,
            purchase_price=purchase_price,
            warrantee_expire_date=warrantee_expire_date,
            dealer_id=dealer_id,
        )
        db.session.add(ownership)
        db.session.commit()
        return redirect(url_for("ownerships.customer_ownerships"))
    ownerships = CustomerOwnership.query.all()
    return render_template("customer_ownerships.html", ownerships=ownerships)


@ownerships_bp.route("/customer_ownership/new", methods=["GET", "POST"])
def new_customer_ownership():
    customers = Customer.query.all()
    customers_dict = [
        {
            "customer_id": c.customer_id,
            "first_name": c.first_name,
            "last_name": c.last_name,
        }
        for c in customers
    ]
    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        vin = request.form.get("vin")
        purchase_date = request.form.get("purchase_date")
        purchase_price = request.form.get("purchase_price")
        warrantee_expire_date = request.form.get("warrantee_expire_date")
        dealer_id = request.form.get("dealer_id")
        ownership = CustomerOwnership(
            customer_id=customer_id,
            vin=vin,
            purchase_date=purchase_date,
            purchase_price=purchase_price,
            warrantee_expire_date=warrantee_expire_date,
            dealer_id=dealer_id,
        )
        db.session.add(ownership)
        db.session.commit()
        return redirect(url_for("ownerships.customer_ownerships"))
    return render_template("customer_ownership_form.html", customers=customers_dict)


@ownerships_bp.route(
    "/customer_ownership/<int:customer_id>/<int:vin>", methods=["GET", "POST"]
)
def view_customer_ownership(customer_id, vin):
    ownership = CustomerOwnership.query.get_or_404((customer_id, vin))
    customers = Customer.query.all()
    customers_dict = [
        {
            "customer_id": c.customer_id,
            "first_name": c.first_name,
            "last_name": c.last_name,
        }
        for c in customers
    ]
    if request.method == "POST":
        ownership.customer_id = request.form.get("customer_id")
        ownership.vin = request.form.get("vin")
        ownership.purchase_date = request.form.get("purchase_date")
        ownership.purchase_price = request.form.get("purchase_price")
        ownership.warrantee_expire_date = request.form.get("warrantee_expire_date")
        ownership.dealer_id = request.form.get("dealer_id")
        db.session.commit()
        return redirect(url_for("ownerships.customer_ownerships"))
    return render_template(
        "customer_ownership_form.html", ownership=ownership, customers=customers_dict
    )


@ownerships_bp.route(
    "/customer_ownership/<int:customer_id>/<int:vin>/delete", methods=["POST"]
)
def delete_customer_ownership(customer_id, vin):
    ownership = CustomerOwnership.query.get_or_404((customer_id, vin))
    db.session.delete(ownership)
    db.session.commit()
    return redirect(url_for("ownerships.customer_ownerships"))
