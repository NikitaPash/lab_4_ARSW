from models.customer import Customer
from models.order import Order


class BulkOrder(Order):
    def __init__(self, customer: Customer):
        super().__init__(customer)
        self.discount_percentage = 10

    def calculate_total(self) -> float:
        base_total = sum(dish.price for dish in self.dishes)
        discount = base_total * (self.discount_percentage / 100)
        return base_total - discount

    def __repr__(self):
        return f"BulkOrder(customer={self.customer}, dishes={self.dishes}, discount={self.discount_percentage}%)"
