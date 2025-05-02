class Customer:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Customer(name={self.name!r})"
