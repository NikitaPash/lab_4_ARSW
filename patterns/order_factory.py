from models.bulk_order import BulkOrder
from models.customer import Customer
from models.order import Order


class OrderFactory:
    @staticmethod
    def create_order(type: str, customer: Customer) -> Order:
        if customer is None:
            raise ValueError("Customer cannot be None")

        if type is None:
            raise AttributeError("Order type cannot be None")

        if type.lower() == "bulk":
            return BulkOrder(customer)
        else:
            return Order(customer)
