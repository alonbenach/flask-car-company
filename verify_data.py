from code.app import app, db
from code.models import Customer, CustomerOwnership, CarVin, CarModel, Brand, Dealer


def verify_data():
    with app.app_context():
        customers = Customer.query.all()
        ownerships = CustomerOwnership.query.all()
        vins = CarVin.query.all()
        models = CarModel.query.all()
        brands = Brand.query.all()
        dealers = Dealer.query.all()

        print("Customers:")
        for customer in customers:
            print(
                f"ID: {customer.customer_id}, Name: {customer.first_name} {customer.last_name}"
            )

        print("\nCustomer Ownerships:")
        for ownership in ownerships:
            print(
                f"Customer ID: {ownership.customer_id}, VIN: {ownership.vin}, Purchase Date: {ownership.purchase_date}"
            )

        print("\nVINs:")
        for vin in vins:
            print(f"VIN: {vin.vin}, Model ID: {vin.model_id}")

        print("\nModels:")
        for model in models:
            print(f"Model ID: {model.model_id}, Name: {model.model_name}")

        print("\nBrands:")
        for brand in brands:
            print(f"Brand ID: {brand.brand_id}, Name: {brand.brand_name}")

        print("\nDealers:")
        for dealer in dealers:
            print(f"Dealer ID: {dealer.dealer_id}, Name: {dealer.dealer_name}")


if __name__ == "__main__":
    verify_data()
