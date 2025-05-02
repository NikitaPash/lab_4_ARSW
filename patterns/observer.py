from abc import ABC, abstractmethod


class KitchenNotifier(ABC):
    @abstractmethod
    def notify(self, order):
        pass


class OrderSubject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: KitchenNotifier):
        self._observers.append(observer)

    def detach(self, observer: KitchenNotifier):
        self._observers.remove(observer)

    def notify_all(self, order):
        for obs in self._observers:
            obs.notify(order)
