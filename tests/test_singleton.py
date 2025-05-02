import pytest

from models.customer import Customer
from models.dish import Dish
from models.order import Order
from patterns.database import Database


def test_singleton_instance():
    """Test that Database.get_instance() always returns the same instance."""
    Database._instance = None

    db1 = Database.get_instance()
    db2 = Database.get_instance()

    assert db1 is db2
    assert db1 == db2


def test_singleton_constructor():
    """Test that the Database constructor raises an exception if called directly after initialization."""
    Database._instance = None

    Database()

    with pytest.raises(Exception) as excinfo:
        Database()

    assert "singleton" in str(excinfo.value).lower()


def test_singleton_add_order():
    """Test that orders can be added to the database."""
    Database._instance = None

    db = Database.get_instance()
    customer = Customer("Alice")
    order = Order(customer)
    order.add_dish(Dish("Pizza", 150))

    db.add_order(order)

    assert len(db.orders) == 1
    assert db.orders[0] == order


def test_singleton_list_orders():
    """Test that orders can be listed from the database."""
    Database._instance = None

    db = Database.get_instance()
    customer1 = Customer("Bob")
    order1 = Order(customer1)
    order1.add_dish(Dish("Burger", 120))

    customer2 = Customer("Charlie")
    order2 = Order(customer2)
    order2.add_dish(Dish("Salad", 80))

    db.add_order(order1)
    db.add_order(order2)

    orders = db.list_orders()

    assert len(orders) == 2
    assert orders[0] == order1
    assert orders[1] == order2


def test_singleton_persistence():
    """Test that the database persists orders between different instances."""
    Database._instance = None

    db1 = Database.get_instance()
    customer = Customer("David")
    order = Order(customer)
    order.add_dish(Dish("Pasta", 130))
    db1.add_order(order)

    db2 = Database.get_instance()
    assert len(db2.orders) == 1
    assert db2.orders[0] == order


def test_singleton_empty_database():
    """Test that a new database instance has no orders."""
    Database._instance = None

    db = Database.get_instance()
    assert len(db.orders) == 0
    assert db.list_orders() == []
