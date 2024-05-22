from flask import Blueprint, request, render_template, redirect, url_for, flash
from ..models import db, Customer, CustomerOwnership

customers_bp = Blueprint("customers", __name__)


@customers_bp.route("/customers", methods=["GET", "POST"])
def customers():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        gender = request.form.get("gender")
        household_income = request.form.get("household_income")
        birthdate = request.form.get("birthdate")
        phone_number = request.form.get("phone_number")
        email = request.form.get("email")
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            household_income=household_income,
            birthdate=birthdate,
            phone_number=phone_number,
            email=email,
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
        gender = request.form.get("gender")
        household_income = request.form.get("household_income")
        birthdate = request.form.get("birthdate")
        phone_number = request.form.get("phone_number")
        email = request.form.get("email")
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            household_income=household_income,
            birthdate=birthdate,
            phone_number=phone_number,
            email=email,
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
        customer.gender = request.form.get("gender")
        customer.household_income = request.form.get("household_income")
        customer.birthdate = request.form.get("birthdate")
        customer.phone_number = request.form.get("phone_number")
        customer.email = request.form.get("email")
        db.session.commit()
        return redirect(url_for("customers.customers"))
    return render_template("customer_form.html", customer=customer)


@customers_bp.route("/customer/<int:customer_id>/delete", methods=["POST"])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    try:
        if CustomerOwnership.query.filter_by(customer_id=customer_id).count() > 0:
            raise ValueError("Customer has assigned ownerships and cannot be deleted.")
        db.session.delete(customer)
        db.session.commit()
        flash("Customer deleted successfully.", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect(url_for("customers.customers"))
