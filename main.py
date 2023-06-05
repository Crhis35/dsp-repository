

from entities.sheep import Sheep


sheep = Sheep('Lucas', 5, 'I am a sheep',  0)

print(sheep.description)
new_sheep = sheep.clone()
new_sheep2 = sheep.clone()
new_sheep3 = sheep.clone()
new_sheep4 = sheep.clone()
sheep.description = 'I am not a sheep'
print(sheep.description)

print(new_sheep.description)
