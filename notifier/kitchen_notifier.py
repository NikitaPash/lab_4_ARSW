from patterns.observer import KitchenNotifier


class KitchenObserver(KitchenNotifier):
    def notify(self, order):
        dishes_str = ", ".join([f"{dish.name} (${dish.price})" for dish in order.dishes])

        if hasattr(order, 'discount_percentage'):
            print(f"Kitchen notified of new order: Bulk Order for {order.customer.name} with {order.discount_percentage}% discount")
        else:
            print(f"Kitchen notified of new order: Standard Order for {order.customer.name}")

        print(f"Items: {dishes_str}")
