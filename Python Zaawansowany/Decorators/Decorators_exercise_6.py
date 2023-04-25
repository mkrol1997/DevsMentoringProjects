from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Car:
    owner: ClassVar[str] = 'OwnerName'
    _brand: str
    _power: int

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, new_power):
        self._power = new_power

    @staticmethod
    def give_a_ride(passenger: str):
        print(f'You just gave {passenger} a ride')

    @classmethod
    def sell_all_cars(cls, sell_to: str):
        cls.owner = sell_to
