from typing import List

from .dish import Dish


class Menu:
    def __init__(self):
        self._dishes: List[Dish] = []

    def add_dish(self, dish: Dish):
        self._dishes.append(dish)

    def contains_dish(self, dish: Dish) -> bool:
        return dish in self._dishes

    def list_dishes(self) -> list[Dish]:
        return list(self._dishes)
