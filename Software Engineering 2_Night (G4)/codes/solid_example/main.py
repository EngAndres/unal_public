from person import Person
from concretes import Unal, Barranquilla, Bogota, Medellin
from typing import List

population:List[Person] = []

population.append(Barranquilla('Roger'))
population.append(Bogota('Bryan'))
population.append(Medellin('Esteban'))
population.append(Unal('Juan'))

for p in population:
    p.eat()
