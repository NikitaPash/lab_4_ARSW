from patterns.observer import OrderSubject
from .customer import Customer
from .dish import Dish


class Order(OrderSubject):
    def __init__(self, customer: Customer):
        super().__init__()
        self.customer = customer
        self.dishes: list[Dish] = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)
        self.notify_all(self)

    def calculate_total(self) -> float:
        return sum(dish.price for dish in self.dishes)

    def __repr__(self):
        return f"Order(customer={self.customer}, dishes={self.dishes})"
