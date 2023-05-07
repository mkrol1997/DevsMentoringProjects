from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Car:
    owner: ClassVar[str] = 'OwnerName'
    _brand: str
    _power: int

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, new_brand) -> None:
        self._brand = new_brand

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, new_power: int) -> None:
        self._power = new_power

    @staticmethod
    def give_a_ride(passenger: str) -> None:
        print(f'You just gave {passenger} a ride')

    @classmethod
    def sell_all_cars(cls, sell_to: str) -> None:
        cls.owner = sell_to
