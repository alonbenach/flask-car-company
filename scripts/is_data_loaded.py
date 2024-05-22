from code.app import app, db
from code.models import CustomerOwnership

with app.app_context():
    ownerships = CustomerOwnership.query.all()
    for ownership in ownerships:
        print(
            f"Customer ID: {ownership.customer_id}, VIN: {ownership.vin}, Purchase Date: {ownership.purchase_date}"
        )
