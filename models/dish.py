class Dish:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return isinstance(other, Dish) and self.name == other.name and self.price == other.price

    def __repr__(self):
        return f"Dish(name={self.name!r}, price={self.price})"
