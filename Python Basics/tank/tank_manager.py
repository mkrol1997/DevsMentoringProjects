from __future__ import annotations

import time
import inspect

from tank import Tank, VolumeExceededLimitError
from tank_special_methods import TankSpecialMethods, NoTanksInitializedError
from registry import Registry


class TankManager:

    def __init__(self) -> None:
        self.all_tanks = [Tank('Tank_1', 2000), Tank('Tank_2', 2000), Tank('Tank_3', 2500)]
        self.registry = Registry(self.all_tanks)


    def pour_water(self, tank_name: str, volume):
        time.sleep(1)
        try:
            requested_tank = list(filter(lambda tank: tank.name == tank_name, self.all_tanks))
            if len(requested_tank) == 0:
                raise KeyError(f'Tank {tank_name} not found in the system')

            requested_tank[0].pour_water(volume)

        except (IndexError, TypeError, VolumeExceededLimitError) as err:
            print(err)
            operation_status = False
        else:
            operation_status = True

        finally:
            try:
                self.registry.register_operation(
                    operation_name=inspect.stack()[0].function,
                    tank_name=tank_name,
                    volume=volume,
                    status=operation_status)
            except UnboundLocalError:
                pass


    def pour_out_water(self, tank_name: str, volume: int) -> None:
        time.sleep(1)
        try:
            requested_tank = list(filter(lambda tank: tank.name == tank_name, self.all_tanks))
            if len(requested_tank) == 0:
                raise KeyError(f'Tank {tank_name} not found in the system')

            requested_tank[0].pour_out_water(volume)

        except (IndexError, TypeError, VolumeExceededLimitError) as err:
            print(err)
            operation_status = False
        else:
            operation_status = True

        finally:
            try:
                self.registry.register_operation(
                    operation_name=inspect.stack()[0].function,
                    tank_name=tank_name,
                    volume=volume,
                    status=operation_status)
            except UnboundLocalError:
                pass


    def transfer_water(self, from_tank, to_tank: str, volume: int):
        TankManager.pour_out_water(self, from_tank, volume)
        TankManager.pour_water(self, to_tank, volume)


    def tank_with_the_most_water(self):
        try:
            return TankSpecialMethods.tank_with_the_most_water(self.all_tanks)
        except NoTanksInitializedError as err:
            print(err)

    def tank_with_the_most_water_percentage(self):
        try:
            return TankSpecialMethods.tank_with_the_most_water_percentage(self.all_tanks)
        except NoTanksInitializedError as err:
            print(err)

    def find_empty_tanks(self):
        try:
            return TankSpecialMethods.find_empty_tanks(self.all_tanks)
        except NoTanksInitializedError as err:
            print(err)

    def tank_with_the_most_failed_operations(self) -> Tank:
        try:
            searched_tank = TankSpecialMethods.tank_with_the_most_failed_operations(
                tanks=self.all_tanks,
                registry=self.registry.registry)

        except Exception as err:
            print(err)
        else:
            return searched_tank

    def tank_with_the_most_performed_operations(self, operation_name: str) -> Tank:
        try:
            searched_tank = TankSpecialMethods.tank_with_the_most_performed_operations(
                operation_name=operation_name,
                registry=self.registry.registry,
                tanks=self.all_tanks)

        except Exception as err:
            print(err)
        else:
            return searched_tank


if __name__ == '__main__':
    manager = TankManager()
