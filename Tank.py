import inspect
from datetime import datetime


class Tank:
    all_tanks = []
    registry = {}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.tank_filling = 0
        # Add tank object to the list of all tanks
        Tank.all_tanks.append(self)
        # Initialize registry key for created tank
        Tank.registry[name] = {}

    def __repr__(self):
        return f'{self.name}: {self.tank_filling}/{self.capacity} L'

    def pour_water(self, volume: int):
        try:
            # Volume left inside the tank
            space_left = self.capacity - self.tank_filling
            if space_left < volume:
                print(f'There is not enough space in {self.name}\n'
                      f'Please try different tank.\n')
                operation_status = False
            else:
                self.tank_filling += volume
                operation_status = True

        except TypeError:
            print("Volume must be an integer.\n")
        else:
            # Register operation
            Tank.__register__(
                operation_name=inspect.stack()[0].function,
                tank_name=self.name,
                volume=volume,
                status=operation_status)

    def pour_out_water(self, volume: int):
        try:
            if self.tank_filling - volume < 0:
                print(f'There is not enough water in {self.name}.\n'
                      f'Please try different tank.\n')
                operation_status = False
            else:
                self.tank_filling -= volume
                operation_status = True
        except TypeError:
            print("Volume must be an integer.\n")
        else:
            # Register operation
            Tank.__register__(
                operation_name=inspect.stack()[0].function,
                tank_name=self.name,
                volume=volume,
                status=operation_status)

    def transfer_water(self, from_tank, volume: int):
        from_tank.pour_out_water(volume)
        self.pour_water(volume)

    @classmethod
    def tank_with_the_most_water(cls):
        try:
            if len(cls.all_tanks) <= 1:
                # Either one or none tank has been initialized yet
                # Raise IndexError if there are no tanks
                return print(cls.all_tanks[0])
            else:
                # Assing first tank object from tanks list to a variable
                result = cls.all_tanks[0]
                for tank in cls.all_tanks[1:]:  # Start iteration from second tank
                    if tank.tank_filling > result.tank_filling:
                        result = tank

        except IndexError:
            print("There are to Tanks initialized.")
        else:
            print(result)

    @classmethod
    def tank_with_the_most_water_percentage(cls):
        # Counts percentage of the fillement of each tank -> 0-100 %
        try:
            if len(cls.all_tanks) <= 1:
                # Only one or no tank has been initialized yet
                # Raise IndexError if there are no tanks
                return print(cls.all_tanks[0])
            else:
                # Assing first tank object from tanks list to a variable
                result = cls.all_tanks[0]
                for tank in cls.all_tanks[1:]:
                    if tank.tank_filling > result.tank_filling:
                        result = tank
                print(result)

        except IndexError:
            print("There are to Tanks initialized.")
        else:
            print(result)

    @classmethod
    def find_empty_tanks(cls):
        if len(cls.all_tanks) == 0:
            print("There are to Tanks initialized.")
        else:
            print("Empty tanks: ", end="")
            print(*list(tank.name for tank in cls.all_tanks
                        if tank.tank_filling == 0), sep=', ')

    @classmethod
    def the_most_failed_operations(cls):
        failed_operations = {}
        for tank_registry_data in cls.registry.values():
            for operation_data in tank_registry_data.values():
                # operation_data -> ['tank_name', 'operation', volume, status]
                try:
                    if not operation_data[-1]:
                        failed_operations[operation_data[1]] += 1
                except KeyError:
                    failed_operations[operation_data[1]] = 1
        try:
            # Sort {tank_name: failed_operations_count}
            # by count of failed operations
            result = sorted(failed_operations.items(),
                            key=lambda x: x[1], reverse=True)[0]
        except IndexError:
            print("Failed operation hasn't been performed on any of the tanks yet.")
        else:
            print(f'{result[0]} - Failed operations: {result[1]}')

    @classmethod
    def the_most_performed_operations(cls, operation_name):
        operation_count = {}

        for tank_registry_data in cls.registry.values():
            for operation_data in tank_registry_data.values():
                # operation_data -> ['tank_name', 'operation', volume, status]
                try:
                    if operation_data[0] == operation_name:
                        operation_count[operation_data[1]] += 1
                except KeyError:
                    operation_count[operation_data[1]] = 1

        try:
            # Sort {tank_name: performed_operation_count}
            # by failed operations count
            result = sorted(operation_count.items(),
                            key=lambda x: x[1], reverse=True)[0]
        except IndexError:
            print(f"Operation '{operation_name}' hasn't been "
                  f"performed on any of the tanks.")
        else:
            print(f"{result[0]} - Action '{operation_name}' "
                  f"performed {result[1]} times")

    @classmethod
    def __register__(cls, operation_name, tank_name, volume, status):
        date = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        # Packing and unpacking operations in order / Sorted by the latest date
        cls.registry[tank_name] = {
                                **{date: [operation_name, tank_name, volume, status]},
                                **cls.registry[tank_name]
                                }

    @classmethod
    def check_state(cls, tank_name):
        water_status = 0

        for operation in cls.registry[tank_name].values():
            if operation[-1] and operation[0] == "pour_water":
                water_status += operation[2]
            elif operation[-1] and operation[0] == "pour_out_water":
                water_status -= operation[2]

        # Search for tank in tanks list and compare state
        for tank in cls.all_tanks:
            if tank.name == tank_name:
                if water_status == tank.tank_filling:
                    return True
                else:
                    return False

def main():
    # Instantiate tanks
    tank_one = Tank('Tank no.1', 1000)
    tank_two = Tank('Tank no.2', 1000)
    tank_three = Tank('Tank no.3', 1500)
    tank_four = Tank('Tank no.4', 2000)

    # Performe actions on tanks
    tank_one.pour_water(100)
    tank_three.pour_water(1000)
    tank_one.transfer_water(tank_three, 250)
    tank_two.pour_water(200)
    tank_two.pour_water(100)
    tank_two.pour_water(100)
    tank_two.pour_water(100)
    tank_two.pour_water(100)
    tank_two.pour_water(100)
    tank_two.pour_out_water(10000)
    tank_two.pour_out_water(9999)
    tank_one.pour_water(100000)
    tank_three.pour_water(10000)
    tank_two.pour_out_water(150)
    tank_two.pour_water(300)
    tank_four.pour_out_water(100)

    print(Tank.registry)
    print(Tank.check_state("Tank no.2"))


if __name__ == "__main__":
    main()
