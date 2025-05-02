from models.bulk_order import BulkOrder
from models.customer import Customer
from models.dish import Dish
from models.order import Order


def test_order_creation():
    """Test that an order can be created with a customer."""
    customer = Customer("Alice")
    order = Order(customer)
    assert order.customer.name == "Alice"
    assert len(order.dishes) == 0


def test_order_add_dish():
    """Test that dishes can be added to an order."""
    customer = Customer("Bob")
    order = Order(customer)
    dish = Dish("Pasta", 120)
    order.add_dish(dish)
    assert len(order.dishes) == 1
    assert order.dishes[0].name == "Pasta"


def test_order_calculate_total():
    """Test that the order total is calculated correctly."""
    customer = Customer("Charlie")
    order = Order(customer)
    order.add_dish(Dish("Salad", 80))
    order.add_dish(Dish("Steak", 250))
    assert order.calculate_total() == 330


def test_bulk_order_creation():
    """Test that a bulk order can be created with a customer."""
    customer = Customer("David")
    order = BulkOrder(customer)
    assert order.customer.name == "David"
    assert len(order.dishes) == 0
    assert order.discount_percentage == 10


def test_bulk_order_calculate_total():
    """Test that the bulk order total is calculated correctly with discount."""
    customer = Customer("Eve")
    order = BulkOrder(customer)
    order.add_dish(Dish("Pizza", 100))
    order.add_dish(Dish("Burger", 90))
    assert order.calculate_total() == 171


def test_bulk_order_custom_discount():
    """Test that the bulk order discount can be customized."""
    customer = Customer("Frank")
    order = BulkOrder(customer)
    order.discount_percentage = 20
    order.add_dish(Dish("Lobster", 300))
    assert order.calculate_total() == 240


def test_empty_order_total():
    """Test that an empty order has zero total."""
    customer = Customer("Grace")
    order = Order(customer)
    assert order.calculate_total() == 0


def test_empty_bulk_order_total():
    """Test that an empty bulk order has zero total."""
    customer = Customer("Hank")
    order = BulkOrder(customer)
    assert order.calculate_total() == 0
