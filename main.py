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

    # Create and display menu
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

    # Check if menu contains specific dishes
    pizza = Dish("Pizza", 150)
    if menu.contains_dish(pizza):
        print(f"Menu contains {pizza.name}\n")

    # Create a standard order
    print("Creating a standard order...")
    alice = Customer("Alice")
    standard_order = OrderFactory.create_order("standard", alice)

    # Set up notification
    kitchen = KitchenObserver()
    standard_order.attach(kitchen)

    # Add dishes to standard order
    print("Adding dishes to Alice's order...")
    standard_order.add_dish(Dish("Pizza", 150))
    standard_order.add_dish(Dish("Sushi", 200))

    # Calculate and display total
    total = standard_order.calculate_total()
    print(f"Total for Alice's order: ${total}\n")

    # Create a bulk order with discount
    print("Creating a bulk order with discount...")
    bob = Customer("Bob")
    bulk_order = OrderFactory.create_order("bulk", bob)
    bulk_order.attach(kitchen)

    # Add dishes to bulk order
    print("Adding dishes to Bob's bulk order...")
    bulk_order.add_dish(Dish("Burger", 120))
    bulk_order.add_dish(Dish("Salad", 80))
    bulk_order.add_dish(Dish("Pizza", 150))

    # Calculate and display total with discount
    bulk_total = bulk_order.calculate_total()
    original_total = sum(dish.price for dish in bulk_order.dishes)
    print(f"Original total for Bob's order: ${original_total}")
    print(f"Discounted total ({bulk_order.discount_percentage}% off): ${bulk_total}\n")

    # Store orders in database
    print("Storing orders in database...")
    db = Database.get_instance()
    db.add_order(standard_order)
    db.add_order(bulk_order)

    # Display all orders in database
    print("\nCurrent orders in DB:")
    for i, order in enumerate(db.list_orders(), 1):
        if hasattr(order, 'discount_percentage'):
            print(f"{i}. {format_bulk_order(order)}")
        else:
            print(f"{i}. {format_order(order)}")


if __name__ == "__main__":
    main()
