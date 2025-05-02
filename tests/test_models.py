from models.customer import Customer
from models.dish import Dish
from models.menu import Menu


def test_create_dish():
    d = Dish("Burger", 100)
    assert d.name == "Burger"
    assert d.price == 100


def test_menu_add_and_contains():
    menu = Menu()
    dish = Dish("Pizza", 150)
    menu.add_dish(dish)
    assert menu.contains_dish(dish)


def test_menu_list_dishes():
    menu = Menu()
    dish1 = Dish("Pizza", 150)
    dish2 = Dish("Sushi", 200)
    menu.add_dish(dish1)
    menu.add_dish(dish2)
    assert menu.list_dishes() == [dish1, dish2]


def test_customer_creation():
    c = Customer("Bob")
    assert c.name == "Bob"
