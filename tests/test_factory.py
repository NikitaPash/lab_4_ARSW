import pytest

from models.bulk_order import BulkOrder
from models.customer import Customer
from models.order import Order
from patterns.order_factory import OrderFactory


def test_factory_creates_standard_order():
    """Test that the factory creates a standard order."""
    customer = Customer("Alice")
    order = OrderFactory.create_order("standard", customer)
    assert isinstance(order, Order)
    assert not isinstance(order, BulkOrder)
    assert order.customer.name == "Alice"


def test_factory_creates_bulk_order():
    """Test that the factory creates a bulk order."""
    customer = Customer("Bob")
    order = OrderFactory.create_order("bulk", customer)
    assert isinstance(order, BulkOrder)
    assert order.customer.name == "Bob"
    assert order.discount_percentage == 10


def test_factory_case_insensitive():
    """Test that the factory is case-insensitive for order types."""
    customer = Customer("Charlie")
    order1 = OrderFactory.create_order("BULK", customer)
    order2 = OrderFactory.create_order("bulk", customer)
    assert isinstance(order1, BulkOrder)
    assert isinstance(order2, BulkOrder)


def test_factory_default_to_standard():
    """Test that the factory defaults to standard order for unknown types."""
    customer = Customer("David")
    order = OrderFactory.create_order("unknown", customer)
    assert isinstance(order, Order)
    assert not isinstance(order, BulkOrder)


def test_factory_empty_type():
    """Test that the factory handles empty type string."""
    customer = Customer("Eve")
    order = OrderFactory.create_order("", customer)
    assert isinstance(order, Order)
    assert not isinstance(order, BulkOrder)


def test_factory_none_type():
    """Test that the factory handles None type."""
    customer = Customer("Frank")
    with pytest.raises(AttributeError):
        OrderFactory.create_order(None, customer)
