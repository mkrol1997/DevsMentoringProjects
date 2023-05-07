from __future__ import annotations


class Order:
    def __init__(self, name: str, price: str) -> None:
        self.id = int
        self.name = name
        self.price = price

    def __hash__(self) -> int:
        return hash((self.name, self.price))

    def __eq__(self, other: Order) -> bool:
        return (self.name, self.price) == (other.name, other.price)

    def __str__(self) -> str:
        return f'{self.name}; {self.price}'


class OrderManager:
    def __init__(self) -> None:
        self.orders = dict()
        self.new_id = 1

    def __str__(self) -> str:
        return f'{self.orders}'

    def add_order(self, order_to_add: Order) -> None:
        for order in self.orders:
            if order == order_to_add:
                self.orders[order] += 1
                return

        self.orders[order_to_add] = 1
        order_to_add.id = self.new_id
        self.new_id += 1

    def sell_order(self, id_to_sell: int) -> None:
        for order in self.orders:
            if order.id == id_to_sell:
                if self.orders[order] > 1:
                    self.orders[order] -= 1
                else:
                    self.orders.pop(order)
                    break


def main():
    manager = OrderManager()
    manager.add_order(Order('Apples', '14.99$'))
    manager.sell_order(1)


if __name__ == "__main__":
    main()
