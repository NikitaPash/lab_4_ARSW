from models.order import Order


class Database:
    _instance = None

    def __init__(self):
        if Database._instance is not None:
            raise Exception("This class is a singleton!")
        self.orders = []
        Database._instance = self

    @staticmethod
    def get_instance():
        if Database._instance is None:
            Database()
        return Database._instance

    def add_order(self, order: Order):
        self.orders.append(order)

    def list_orders(self):
        return list(self.orders)
