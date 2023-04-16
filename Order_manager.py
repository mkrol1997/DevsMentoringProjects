class Order:
    def __init__(self, name, price):
        self.id = int
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}; {self.price}'


class Manager:
    def __init__(self):
        self.orders = dict()
        # Object id starting from 1
        self.new_id = 1

    def __repr__(self):
        return f'{self.orders}'

    def add_order(self, order_to_add):
        for order in self.orders:
            if order.name == order_to_add.name:
                self.orders[order] += 1
                return None

        # Add a new order to dict of orders
        self.orders[order_to_add] = 1
        # Assing auto-incremented id to the new order
        order_to_add.id = self.new_id
        self.new_id += 1

    def sell_order(self, id_to_sell):
        for order in self.orders:
            if order.id == id_to_sell:
                if self.orders[order] > 1:
                    self.orders[order] -= 1
                else:
                    self.orders.pop(order)
                    break


def main():
    manager = Manager()

    manager.add_order(Order('Apples', '14.99$'))
    manager.add_order(Order('Apples', '14.99$'))
    manager.add_order(Order('Apples', '14.99$'))
    manager.add_order(Order('Bananas', '9.99$'))
    manager.add_order(Order('Bananas', '9.99$'))
    manager.add_order(Order('Grapes', '9.99$'))
    manager.add_order(Order('Cucumber', '9.99$'))
    print(manager)

    manager.sell_order(1)
    manager.sell_order(3)
    print(manager)


if __name__ == "__main__":
    main()
