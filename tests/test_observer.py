from models.customer import Customer
from models.dish import Dish
from models.order import Order
from notifier.kitchen_notifier import KitchenObserver
from patterns.observer import KitchenNotifier


class MockKitchenNotifier(KitchenNotifier):
    """A mock kitchen notifier for testing."""

    def __init__(self):
        self.notified = False
        self.last_order = None

    def notify(self, order):
        self.notified = True
        self.last_order = order


def test_attach_observer():
    """Test that an observer can be attached to an order."""
    customer = Customer("Alice")
    order = Order(customer)
    notifier = MockKitchenNotifier()
    order.attach(notifier)
    assert notifier in order._observers


def test_detach_observer():
    """Test that an observer can be detached from an order."""
    customer = Customer("Bob")
    order = Order(customer)
    notifier = MockKitchenNotifier()
    order.attach(notifier)
    order.detach(notifier)
    assert notifier not in order._observers


def test_notify_observers():
    """Test that all observers are notified when a dish is added."""
    customer = Customer("Charlie")
    order = Order(customer)
    notifier1 = MockKitchenNotifier()
    notifier2 = MockKitchenNotifier()
    order.attach(notifier1)
    order.attach(notifier2)

    order.add_dish(Dish("Pizza", 150))

    assert notifier1.notified
    assert notifier2.notified
    assert notifier1.last_order == order
    assert notifier2.last_order == order


def test_notify_with_multiple_dishes():
    """Test that observers are notified each time a dish is added."""
    customer = Customer("David")
    order = Order(customer)
    notifier = MockKitchenNotifier()
    order.attach(notifier)

    order.add_dish(Dish("Salad", 80))
    assert notifier.notified
    assert notifier.last_order == order

    notifier.notified = False
    order.add_dish(Dish("Steak", 250))
    assert notifier.notified
    assert notifier.last_order == order


def test_no_observers():
    """Test that adding a dish works even with no observers."""
    customer = Customer("Eve")
    order = Order(customer)

    order.add_dish(Dish("Burger", 120))
    assert len(order.dishes) == 1


def test_kitchen_observer_implementation(capsys):
    """Test the actual KitchenObserver implementation."""
    customer = Customer("Frank")
    order = Order(customer)
    notifier = KitchenObserver()
    order.attach(notifier)

    order.add_dish(Dish("Pasta", 130))

    captured = capsys.readouterr()
    assert "Kitchen notified of new order" in captured.out
    assert "Frank" in captured.out
