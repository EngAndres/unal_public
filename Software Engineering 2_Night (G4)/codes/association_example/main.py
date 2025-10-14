from car import Car
from associations import Sticker, Engine

engine = Engine('Maseratti', 5000)
my_cacharrito = Car(engine)

my_cacharrito.add_sticker(Sticker('I <3 UNAL', 'green'))
my_cacharrito.add_sticker(Sticker('OrgulloUNAL', 'red'))

my_cacharrito.print_car()