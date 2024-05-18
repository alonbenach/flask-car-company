from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, Customer

customers_bp = Blueprint("customers", __name__)


@customers_bp.route("/customers", methods=["GET", "POST"])
def customers():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
        )
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for("customers.customers"))
    customers = Customer.query.all()
    return render_template("customers.html", customers=customers)


@customers_bp.route("/customer/new", methods=["GET", "POST"])
def new_customer():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
        )
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for("customers.customers"))
    return render_template("customer_form.html")


@customers_bp.route("/customer/<int:customer_id>", methods=["GET", "POST"])
def view_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    if request.method == "POST":
        customer.first_name = request.form.get("first_name")
        customer.last_name = request.form.get("last_name")
        customer.email = request.form.get("email")
        customer.phone_number = request.form.get("phone_number")
        db.session.commit()
        return redirect(url_for("customers.customers"))
    return render_template("customer_form.html", customer=customer)


@customers_bp.route("/customer/<int:customer_id>/delete", methods=["POST"])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("customers.customers"))
