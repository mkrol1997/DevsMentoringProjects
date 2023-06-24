from __future__ import annotations
from typing import List
from tank import Tank, VolumeLimitExceededError


class NoTanksInitializedError(Exception):
    pass


class TankSpecialMethods:
    @staticmethod
    def find_tank(tank_name: str, all_tanks: List[Tank]) -> Tank:
        requested_tank = list(filter(lambda tank: tank.name == tank_name, all_tanks))

        if not requested_tank:
            raise KeyError(f'Tank {tank_name} not found in the system')

        return requested_tank[0]

    @staticmethod
    def validate_tanks_before_water_transfer(
            from_name: str, to_name: str, volume: int, tanks: List[Tank]) -> None:
        if not isinstance(volume, int):
            raise TypeError("Volume must be an integer.")

        from_tank = TankSpecialMethods.find_tank(from_name, tanks)
        to_tank = TankSpecialMethods.find_tank(to_name, tanks)

        if from_tank.volume_filling <= volume:
            raise VolumeLimitExceededError(
                f'There is not enough water in'
                f' {from_name}\nPlease try different tank.\n')

        elif to_tank.capacity - to_tank.volume_filling < volume:
            raise VolumeLimitExceededError(
                f'There is not enough space in {to_name}\n'
                f'Please try different tank.\n')

    @staticmethod
    def tank_with_the_most_water(tanks: List[Tank]) -> Tank:
        if not tanks:
            raise NoTanksInitializedError('No tanks initialized yet')

        most_filled_tank = sorted(tanks, key=lambda tank: tank.volume_filling,
                                  reverse=True)[0]

        return most_filled_tank

    @staticmethod
    def tank_with_the_most_water_percentage(tanks: List[Tank]) -> Tank:
        if not tanks:
            raise NoTanksInitializedError('No tanks initialized yet')

        most_filled_tank = sorted(tanks, key=lambda tank:
                                  tank.volume_filling / tank.capacity * 100,
                                  reverse=True)[0]

        return most_filled_tank

    @staticmethod
    def find_empty_tanks(tanks: List[Tank]) -> List[Tank]:
        if not tanks:
            raise NoTanksInitializedError

        empty_tanks = list(filter(lambda tank: tank.volume_filling == 0, tanks))

        if not empty_tanks:
            print('There are no empty tanks available')

        return empty_tanks

    @staticmethod
    def tank_with_the_most_failed_operations(tanks: List[Tank], registry: dict) -> Tank:
        failed_operations = {}

        for all_operations_performed in registry.values():
            for single_operation_data in all_operations_performed.values():

                try:
                    if not single_operation_data['status']:
                        failed_operations[single_operation_data['tank_name']] += 1
                except KeyError:
                    failed_operations[single_operation_data['tank_name']] = 1
                except TypeError:
                    pass

        if not failed_operations:
            raise Exception("Failed operation hasn't"
                            " been performed on any of the tanks yet.")

        tank_name = max(failed_operations, key=failed_operations.get)
        searched_tank = TankSpecialMethods.find_tank(tank_name, tanks)

        return searched_tank

    @staticmethod
    def tank_with_most_performed_operations(registry: dict, tanks: List[Tank]) -> Tank:
        operations_count = {}
        message = 'Choose operation:\n' \
                  '1: pour_water\t2: pour_water_out\n>>> '

        operations_list = {'1': 'pour_water', '2': 'pour_out_water'}

        operation = input(message)
        while operation not in operations_list.keys():
            operation = input(message)

        for all_operations_performed in registry.values():
            for operation_data in all_operations_performed.values():
                try:
                    if operation_data['operation_name'] == operations_list[operation] \
                            and operation_data['status']:
                        operations_count[operation_data['tank_name']] += 1
                except KeyError:
                    operations_count[operation_data['tank_name']] = 1
                except TypeError:
                    pass

        if not operations_count:
            raise Exception("Failed operation hasn't been"
                            " performed on any of the tanks yet.")

        tank_name = max(operations_count, key=operations_count.get)
        searched_tank = TankSpecialMethods.find_tank(tank_name, tanks)

        return searched_tank

    @staticmethod
    def check_state(tank_name: str, tanks: List[Tank], registry: dict) -> bool:
        water_volume = 0

        for operation in registry[tank_name].values():
            try:
                if operation['status'] and operation['operation_name'] == "pour_water":
                    water_volume += operation['volume']
                elif operation['status'] and operation['operation_name'] == "pour_out_water":
                    water_volume -= operation['volume']
            except TypeError:
                pass

        searched_tank = TankSpecialMethods.find_tank(tank_name, tanks)

        return water_volume == searched_tank.volume_filling


if __name__ == '__main__':
    ...
