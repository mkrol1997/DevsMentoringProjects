from __future__ import annotations
from typing import List
from tank import Tank, VolumeLimitExceededError
from tank_special_methods import TankSpecialMethods as spc_meth
from tank_special_methods import NoTanksInitializedError
from registry import Registry
from inspect import stack


class TankManager:

    def __init__(self, *args: Tank) -> None:
        self.all_tanks = [*args]
        self.registry = Registry(self.all_tanks)

    def pour_water(self, tank_name: str, volume: int) -> None:
        try:
            requested_tank = spc_meth.find_tank(tank_name, self.all_tanks)
            operation_status = requested_tank.pour_water(volume)

        except (KeyError, IndexError, TypeError, VolumeLimitExceededError) as err:
            operation_status = False
            print(err)

        finally:
            self.registry.register_operation(
                operation_name=stack()[0].function,
                tank_name=tank_name,
                volume=volume,
                status=operation_status)

    def pour_out_water(self, tank_name: str, volume: int) -> None:
        try:
            requested_tank = spc_meth.find_tank(tank_name, self.all_tanks)
            operation_status = requested_tank.pour_out_water(volume)

        except (KeyError, IndexError, TypeError, VolumeLimitExceededError) as err:
            operation_status = False
            print(err)

        finally:
            self.registry.register_operation(
                operation_name=stack()[0].function,
                tank_name=tank_name,
                volume=volume,
                status=operation_status)

    def transfer_water(self, from_tank, to_tank: str, volume: int) -> None:
        try:
            spc_meth.validate_tanks_before_water_transfer(
                    from_name=from_tank,
                    to_name=to_tank,
                    volume=volume,
                    tanks=self.all_tanks)

        except (KeyError, VolumeLimitExceededError, TypeError) as err:
            print(err)

        else:
            TankManager.pour_out_water(self, from_tank, volume)
            TankManager.pour_water(self, to_tank, volume)

    def tank_with_the_most_water(self) -> Tank:
        try:
            return spc_meth.tank_with_the_most_water(self.all_tanks)

        except NoTanksInitializedError as err:
            print(err)

    def tank_with_the_most_water_percentage(self) -> Tank:
        try:
            return spc_meth.tank_with_the_most_water_percentage(self.all_tanks)

        except NoTanksInitializedError as err:
            print(err)

    def find_empty_tanks(self) -> List[Tank]:
        try:
            return spc_meth.find_empty_tanks(self.all_tanks)

        except NoTanksInitializedError as err:
            print(err)

    def tank_with_the_most_failed_operations(self) -> Tank:
        try:
            return spc_meth.tank_with_the_most_failed_operations(
                        tanks=self.all_tanks,
                        registry=self.registry.registry)

        except Exception as err:
            print(err)


    def tank_with_the_most_performed_operations(self) -> Tank:
        try:
            return spc_meth.tank_with_most_performed_operations(
                        registry=self.registry.registry,
                        tanks=self.all_tanks)

        except Exception as err:
            print(err)

    def check_state(self, tank_name: str) -> bool:
        try:
            return spc_meth.check_state(
                tank_name=tank_name,
                tanks=self.all_tanks,
                registry=self.registry.registry)

        except KeyError:
            print(f'Tank {tank_name} not found in given registry')


if __name__ == '__main__':
    manager = TankManager(Tank('Tank_1', 2500), Tank('Tank_2', 2500))
