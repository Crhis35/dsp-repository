from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Animal(ABC):
    _name: str
    _number_of_legs: int
    _description: str

    @abstractmethod
    def hello_animal(self,) -> None:
        pass

    @abstractmethod
    def clone(self) -> None:
        pass

    @property
    def description(self) -> None:
        return self._description

    @description.setter
    def description(self, description) -> None:
        self._description = description

    @property
    def name(self) -> None:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @property
    def number_of_legs(self) -> None:
        return self._number_of_legs

    @number_of_legs.setter
    def number_of_legs(self, number_of_legs) -> None:
        self._number_of_legs = number_of_legs
