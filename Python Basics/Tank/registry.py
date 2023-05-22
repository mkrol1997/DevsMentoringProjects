from tank import Tank
from typing import List
from datetime import datetime

class Registry:
    def __init__(self, list_of_tanks: List[Tank]) -> None:
        date = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

        self.registry = {tank.name: {date: f'{tank.name} has been added to the system'}
                         for tank in list_of_tanks}


    def register_operation(self, operation_name: str, tank_name: str, volume: int, status: bool) -> None:
        date = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

        self.registry[tank_name] = {
            **{date: {
                "operation_name": operation_name,
                "tank_name": tank_name,
                "volume": volume,
                "status": status}
               },
            **self.registry[tank_name]
            }

    def __str__(self):
        return f'{self.registry}'


if __name__ == "__main__":
    ...
