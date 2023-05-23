from __future__ import annotations
from typing import List
from tank import Tank
from abc import ABC, abstractmethod

class NoTanksInitializedError(Exception):
    pass


class TankSpecialMethods(ABC):
    @staticmethod
    @abstractmethod
    def tank_with_the_most_water(tanks: List[Tank]) -> Tank:
        if len(tanks) == 0:
            raise NoTanksInitializedError

        most_filled_tank = sorted(tanks, key=lambda tank: tank.volume_filling, reverse=True)[0]
        return most_filled_tank


    @staticmethod
    @abstractmethod
    def tank_with_the_most_water_percentage(tanks: List[Tank]) -> Tank:
        if len(tanks) == 0:
            raise NoTanksInitializedError

        most_filled_tank = list(sorted(tanks, key=lambda tank:
                                tank.volume_filling / tank.capacity * 100, reverse=True))[0]

        return most_filled_tank


    @staticmethod
    @abstractmethod
    def find_empty_tanks(tanks: List[Tank]) -> List[Tank]:
        if len(tanks) == 0:
            raise NoTanksInitializedError

        empty_tanks = list(filter(lambda tank: tank.volume_filling == 0, tanks))
        return empty_tanks


    @staticmethod
    @abstractmethod
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
                    # Registry record under consideration is not a performed operation record
                    pass

        if len(failed_operations) == 0:
            raise Exception("Failed operation hasn't been performed on any of the tanks yet.")

        tank_name = max(failed_operations, key=failed_operations.get)
        searched_tank = list(filter(lambda tank: tank.name == tank_name, tanks))[0]

        return searched_tank


    @staticmethod
    @abstractmethod
    def tank_with_the_most_performed_operations(operation_name: str, registry: dict, tanks: List[Tank]) -> Tank:
        operations_count = {}

        for all_operations_performed in registry.values():
            for single_operation_data in all_operations_performed.values():
                try:
                    if single_operation_data['operation_name'] == operation_name \
                            and single_operation_data['status']:
                        operations_count[single_operation_data['tank_name']] += 1
                except KeyError:
                    operations_count[single_operation_data['tank_name']] = 1
                except TypeError:
                    # Registry record under consideration is not a performed operation record
                    pass

        if len(operations_count) == 0:
            raise Exception("Failed operation hasn't been performed on any of the tanks yet.")

        searched_tank = list(filter(lambda tank: tank.name == tank_name, tanks))[0]
        tank_name = max(operations_count, key=operations_count.get)

        return searched_tank


    @staticmethod
    @abstractmethod
    def check_state(tank_name: str, tanks: List[Tank], registry: dict) -> bool:
        water_volume = 0

        for operation in registry[tank_name].values():
            if operation['status'] and operation['operation_name'] == "pour_water":
                water_volume += operation['volume']
            elif operation['status'] and operation['operation_name'] == "pour_out_water":
                water_volume -= operation['volume']

        searched_tank = list(filter(lambda tank: tank.name == tank_name, tanks))

        if len(searched_tank) == 0:
            raise NameError(f'No tank named {tank_name} found in the system')

        if water_volume == searched_tank[0].volume_filling:
            return True
        else:
            return False


if __name__ == '__main__':
    ...

