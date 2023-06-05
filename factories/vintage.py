

from dataclasses import dataclass

from interface.factory import AbstractFactory
from interface.car import Car
from interface.bike import Bike
from entities.vintagebike import VintageBike
from entities.vinategecar import VintageCar


@dataclass
class VintageFactory(AbstractFactory):
    def create_car(self) -> Car:
      return VintageCar()

    def create_bike(self) -> Bike:
      return VintageBike()