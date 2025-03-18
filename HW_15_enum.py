from enum import Enum


class OrderStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    READY = 3
    COMPLETED = 4
    CANCELLED = 5


class Order:
    orders = {}

    def __init__(self, order_id, status=1):
        self.order_id  = order_id
        self.status = status
        self.orders[order_id] = self.status

    def update_status(self, new_status):
        try:
            if new_status in OrderStatus and self.orders[self.order_id] != new_status:
                for state in OrderStatus:
                    if state.value == new_status:
                        self.orders[self.order_id] = new_status
        except AttributeError:
            print('Unknown status!')

    def display_status(self):
        for state in OrderStatus:
            if state.value ==  self.orders[self.order_id]:
                print(f'{state.name}')


ord1 = Order(111, 1)
ord2 = Order(222, 2)

ord1.display_status()
ord1.update_status(5)
print(OrderStatus.name)
