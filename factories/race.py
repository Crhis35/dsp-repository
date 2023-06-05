

from dataclasses import dataclass

from interface.factory import AbstractFactory
from interface.car import Car
from interface.bike import Bike
from entities.racebike import RaceBike
from entities.racecar import RaceCar


@dataclass
class RaceFactory(AbstractFactory):
    def create_car(self) -> Car:
      return RaceCar()

    def create_bike(self) -> Bike:
      return RaceBike()