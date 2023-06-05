from dataclasses import dataclass
from interface.animal import Animal


@dataclass
class Sheep(Animal):
    number_of_clones: int = 0

    def clone(self) -> Animal:
        self.number_of_clones += 1
        print(self.__str__())
        return type(self)(
            self.name,
            self.number_of_clones,
            self.description,
        )

    def hello_animal(self) -> None:
        return super().hello_animal()

    def __str__(self) -> str:
        print('Number of clones: {}'.format(self.number_of_clones))
        return super().__str__()
