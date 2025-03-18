from enum import Enum


class OrderStatus(Enum):
    PENDING = "Заказ ожидает обработки"
    IN_PROGRESS = "Заказ готовится"
    READY = "Заказ готов"
    COMPLETED = "Заказ выдан"
    CANCELLED = "Заказ отменён"


class Order:

    def __init__(self, order_id, status=OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):
        try:
            if isinstance(new_status, OrderStatus):
                self.status = new_status
        except AttributeError as e:
            print(f'Unknown Status!: {e}')

    def display_status(self):
        print(f'Status: {self.status.value}')


ord1 = Order(111)
ord2 = Order(222, OrderStatus.IN_PROGRESS)

ord1.display_status()
ord1.update_status(OrderStatus.READY)
ord1.display_status()
ord1.update_status(OrderStatus.COMPLETED)
ord1.display_status()
