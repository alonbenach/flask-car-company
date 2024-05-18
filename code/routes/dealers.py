from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, Dealer

dealers_bp = Blueprint("dealers", __name__)


@dealers_bp.route("/dealers", methods=["GET", "POST"])
def dealers():
    if request.method == "POST":
        dealer_name = request.form.get("dealer_name")
        dealer_address = request.form.get("dealer_address")
        dealer = Dealer(dealer_name=dealer_name, dealer_address=dealer_address)
        db.session.add(dealer)
        db.session.commit()
        return redirect(url_for("dealers.dealers"))
    dealers = Dealer.query.all()
    return render_template("dealers.html", dealers=dealers)


@dealers_bp.route("/dealer/new", methods=["GET", "POST"])
def new_dealer():
    if request.method == "POST":
        dealer_name = request.form.get("dealer_name")
        dealer_address = request.form.get("dealer_address")
        dealer = Dealer(dealer_name=dealer_name, dealer_address=dealer_address)
        db.session.add(dealer)
        db.session.commit()
        return redirect(url_for("dealers.dealers"))
    return render_template("dealer_form.html")


@dealers_bp.route("/dealer/<int:dealer_id>", methods=["GET", "POST"])
def view_dealer(dealer_id):
    dealer = Dealer.query.get_or_404(dealer_id)
    if request.method == "POST":
        dealer.dealer_name = request.form.get("dealer_name")
        dealer.dealer_address = request.form.get("dealer_address")
        db.session.commit()
        return redirect(url_for("dealers.dealers"))
    return render_template("dealer_form.html", dealer=dealer)


@dealers_bp.route("/dealer/<int:dealer_id>/delete", methods=["POST"])
def delete_dealer(dealer_id):
    dealer = Dealer.query.get_or_404(dealer_id)
    db.session.delete(dealer)
    db.session.commit()
    return redirect(url_for("dealers.dealers"))
