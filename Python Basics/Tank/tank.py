from __future__ import annotations


class VolumeExceededLimitError(Exception):
    pass


class Tank:
    def __init__(self, name: str, capacity: int) -> None:
        self._name = name
        self._capacity = capacity
        self.volume_filling = 0
        print(f'Tank {self._name} added to the system')

    def __str__(self) -> str:
        return f'{self._name}'

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("Name must be a string")

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        if isinstance(capacity, int):
            self._capacity = capacity
        else:
            raise TypeError("Capacity must be an integer")

    def pour_water(self, volume: int) -> None:
        if not isinstance(volume, int):
            raise TypeError("Volume must be an integer.")

        if self.capacity - self.volume_filling < volume:
            raise VolumeExceededLimitError(f'There is not enough space in {self.name}\n'
                  f'Please try different tank.\n')

        self.volume_filling += volume

    def pour_out_water(self, volume: int) -> bool:
        if not isinstance(volume, int):
            raise TypeError("Volume must be an integer.")

        if self.volume_filling - volume < 0:
            raise VolumeExceededLimitError(f'There is not enough water in {self.name}\n'
                                           f'Please try different tank.\n')

        self.volume_filling -= volume


if __name__ == '__main__':
    ...
