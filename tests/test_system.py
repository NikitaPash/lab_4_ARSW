from models.customer import Customer
from models.dish import Dish
from patterns.database import Database
from patterns.order_factory import OrderFactory


def test_full_flow(tmp_path, capsys):
    Database._instance = None
    db = Database.get_instance()

    from models.menu import Menu
    menu = Menu()
    pizza = Dish("Pizza", 150)
    menu.add_dish(pizza)
    assert menu.contains_dish(pizza)

    customer = Customer("Frank")
    order = OrderFactory.create_order("standard", customer)
    order.add_dish(pizza)
    db.add_order(order)

    orders = db.list_orders()
    assert len(orders) == 1
    assert orders[0].customer.name == "Frank"

    import main
    main.main()
    captured = capsys.readouterr()
    assert "Current orders in DB:" in captured.out
