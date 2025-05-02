import pytest

from models.bulk_order import BulkOrder
from models.customer import Customer
from models.dish import Dish
from models.menu import Menu
from models.order import Order
from patterns.order_factory import OrderFactory


def test_dish_equality():
    """Test that dishes with the same name and price are considered equal."""
    dish1 = Dish("Pizza", 150)
    dish2 = Dish("Pizza", 150)
    assert dish1 == dish2


def test_dish_inequality():
    """Test that dishes with different names or prices are not equal."""
    dish1 = Dish("Pizza", 150)
    dish2 = Dish("Pizza", 160)
    dish3 = Dish("Burger", 150)
    assert dish1 != dish2
    assert dish1 != dish3
    assert dish2 != dish3


def test_dish_equality_with_other_types():
    """Test that dishes are not equal to objects of other types."""
    dish = Dish("Pizza", 150)
    assert dish != "Pizza"
    assert dish != 150
    assert dish != {"name": "Pizza", "price": 150}


def test_menu_contains_similar_dish():
    """Test that menu.contains_dish() works with similar dishes."""
    menu = Menu()
    menu.add_dish(Dish("Pizza", 150))

    similar_dish = Dish("Pizza", 150)

    assert menu.contains_dish(similar_dish)


def test_menu_does_not_contain_different_dish():
    """Test that menu.contains_dish() returns False for dishes not in the menu."""
    menu = Menu()
    menu.add_dish(Dish("Pizza", 150))

    different_dish = Dish("Burger", 120)

    assert not menu.contains_dish(different_dish)


def test_order_with_negative_price():
    """Test that an order can handle dishes with negative prices."""
    customer = Customer("Alice")
    order = Order(customer)
    order.add_dish(Dish("Discount Item", -50))
    order.add_dish(Dish("Regular Item", 100))

    assert order.calculate_total() == 50


def test_bulk_order_with_negative_price():
    """Test that a bulk order can handle dishes with negative prices."""
    customer = Customer("Bob")
    order = BulkOrder(customer)
    order.add_dish(Dish("Discount Item", -50))
    order.add_dish(Dish("Regular Item", 100))

    assert order.calculate_total() == 45


def test_bulk_order_with_zero_discount():
    """Test that a bulk order works with zero discount."""
    customer = Customer("Charlie")
    order = BulkOrder(customer)
    order.discount_percentage = 0
    order.add_dish(Dish("Pizza", 100))

    assert order.calculate_total() == 100


def test_bulk_order_with_hundred_percent_discount():
    """Test that a bulk order works with 100% discount."""
    customer = Customer("David")
    order = BulkOrder(customer)
    order.discount_percentage = 100
    order.add_dish(Dish("Pizza", 100))

    assert order.calculate_total() == 0


def test_factory_with_none_customer():
    """Test that the factory raises a ValueError when customer is None."""
    with pytest.raises(ValueError, match="Customer cannot be None"):
        OrderFactory.create_order("standard", None)
