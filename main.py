from models.customer import Customer
from models.dish import Dish
from models.menu import Menu
from notifier.kitchen_notifier import KitchenObserver
from patterns.database import Database
from patterns.order_factory import OrderFactory


def format_order(order):
    """Format an order for user-friendly display"""
    dishes_str = ", ".join([f"{dish.name} (${dish.price})" for dish in order.dishes])
    return f"Order for {order.customer.name}: {dishes_str}"


def format_bulk_order(order):
    """Format a bulk order for user-friendly display"""
    dishes_str = ", ".join([f"{dish.name} (${dish.price})" for dish in order.dishes])
    return f"Bulk Order for {order.customer.name}: {dishes_str} with {order.discount_percentage}% discount"


def main():
    print("===== Restaurant Order Management System =====\n")

    print("Setting up menu...")
    menu = Menu()
    menu.add_dish(Dish("Pizza", 150))
    menu.add_dish(Dish("Sushi", 200))
    menu.add_dish(Dish("Burger", 120))
    menu.add_dish(Dish("Salad", 80))

    print("Menu items:")
    for dish in menu.list_dishes():
        print(f"- {dish.name}: ${dish.price}")
    print()

    pizza = Dish("Pizza", 150)
    if menu.contains_dish(pizza):
        print(f"Menu contains {pizza.name}\n")

    print("Creating a standard order...")
    customer1 = Customer("Potuzhnych")
    standard_order = OrderFactory.create_order("standard", customer1)

    kitchen = KitchenObserver()
    standard_order.attach(kitchen)

    print("Adding dishes to Potuzhnych's order...")
    standard_order.add_dish(Dish("Pizza", 150))
    standard_order.add_dish(Dish("Sushi", 200))

    total = standard_order.calculate_total()
    print(f"Total for Potuzhnych's order: ${total}\n")

    print("Creating a bulk order with discount...")
    customer2 = Customer("Peremozhnych")
    bulk_order = OrderFactory.create_order("bulk", customer2)
    bulk_order.attach(kitchen)

    print("Adding dishes to Peremozhnych's bulk order...")
    bulk_order.add_dish(Dish("Burger", 120))
    bulk_order.add_dish(Dish("Salad", 80))
    bulk_order.add_dish(Dish("Pizza", 150))

    bulk_total = bulk_order.calculate_total()
    original_total = sum(dish.price for dish in bulk_order.dishes)
    print(f"Original total for Peremozhnych's order: ${original_total}")
    print(f"Discounted total ({bulk_order.discount_percentage}% off): ${bulk_total}\n")

    print("Storing orders in database...")
    db = Database.get_instance()
    db.add_order(standard_order)
    db.add_order(bulk_order)

    print("\nCurrent orders in DB:")
    for i, order in enumerate(db.list_orders(), 1):
        if hasattr(order, 'discount_percentage'):
            print(f"{i}. {format_bulk_order(order)}")
        else:
            print(f"{i}. {format_order(order)}")


if __name__ == "__main__":
    main()
