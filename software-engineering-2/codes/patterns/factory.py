class NFS_Factory:

    def __init__(self):
        print("Fábrica de carros de NFS inicializada...")

    def create_car(self, reference, color) -> Car:
        # Liskov Substitution
        new_car: Car = None
        if reference == 'nissan':
            new_car = NissanSkyline(color)
        elif reference == 'porshe':
            new_car = PorsheCarrera(color)
        elif reference == 'chevrolet':
            new_car = ChevroletCorvette(color)
        elif reference == 'shelby':
            new_car = ShelbyCobra(color)
        else:
            raise ValueError("Referencia de carro seleccionada erronea.")
        return new_car
        

#===========

from abc import ABC, abstractmethod

class Car(ABC):
    "Abstract Mother Class"
    
    def __init__(self, color: str):
        self.color: str = color
        self.engine = None
        self.gearbox = None

    @abstractmethod
    def add_engine(self, engine: str):
        pass

    @abstractmethod
    def add_gearbox(self, gearbox: str):
        pass

    def __str__(self):
        return f"Este carro tiene las siguientes especificaciones:\n\
Color: {self.color}\nMotor: {self.engine}\nCaja: {self.gearbox}\n"


# ------ Child Classes ------ #
class NissanSkyline(Car):

    def add_engine(self, engine: str):
        if engine == "gas":
            self.engine = 'V8 Full Injection 5.0'
        elif engine == "electric":
            self.engine = 'EVH 2.0'
        else:
            raise ValueError("Escoja un valor correcto de motor")

    def add_gearbox(self, gearbox: str):
        if gearbox == "6 speeds":
            self.gearbox = 'GB 6 Speed JapanPro'
        elif gearbox == "7 speeds":
            self.gearbox = 'GB 6 Speed JapanPro'
        else:
            raise ValueError("Escoja un valor correcto de caja de cambios")
        
    def __str__(self):
        return "\nEste es un NISSAN SKYLINE.\n" + super().__str__()

class PorsheCarrera(Car):

    def add_engine(self, engine: str):
        if engine == "v10":
            self.engine = 'V10 Atmospheric Porshe Carrera'
        elif engine == "v12":
            self.engine = 'V12 Atmospheric Porshe Carrera'
        else:
            raise ValueError("Escoja un valor correcto de motor")

    def add_gearbox(self, gearbox: str):
        if gearbox == "automatic":
            self.gearbox = 'Automatic Competition GB 6 speed'
        elif gearbox == "semi-automatic":
            self.gearbox = 'Semi-Automatic Competition GB 7 speed'
        else:
            raise ValueError("Escoja un valor correcto de caja de cambios")
        
    def __str__(self):
        return "\nEste es un PORSHE CARRERA.\n" + super().__str__()

class ChevroletCorvette(Car):

    def add_engine(self, engine: str):
        if engine == "v8":
            self.engine = 'V8 LT1 6.2L Chevrolet Corvette'
        elif engine == "v8 supercharged":
            self.engine = 'V8 LT4 6.2L Supercharged Chevrolet Corvette'
        else:
            raise ValueError("Escoja un valor correcto de motor")

    def add_gearbox(self, gearbox: str):
        if gearbox == "manual":
            self.gearbox = 'Tremec TR-6060 Manual 7 Speed'
        elif gearbox == "automatic":
            self.gearbox = 'Paddle-Shift Automatic 8 Speed'
        else:
            raise ValueError("Escoja un valor correcto de caja de cambios")

    def __str__(self):
        return "\nEste es un CHEVROLET CORVETTE.\n" + super().__str__()

class ShelbyCobra(Car):

    def add_engine(self, engine: str):
        if engine == "v8":
            self.engine = 'V8 427 Shelby Cobra'
        elif engine == "v8 supercharged":
            self.engine = 'V8 427 Supercharged Shelby Cobra'
        else:
            raise ValueError("Escoja un valor correcto de motor")

    def add_gearbox(self, gearbox: str):
        if gearbox == "4 speeds":
            self.gearbox = 'Toploader 4 Speed Manual'
        elif gearbox == "5 speeds":
            self.gearbox = 'Tremec T5 5 Speed Manual'
        else:
            raise ValueError("Escoja un valor correcto de caja de cambios")

    def __str__(self):
        return "\nEste es un SHELBY COBRA.\n" + super().__str__()



# ================================== EXAMPLE ============================= #

reference = input("Ingrese una referencia de carro:")
color = input("Ingrese un color: ")

factory = NFS_Factory()
my_car = factory.create_car(reference, color)

engine = input("Qué tipo de motor?:")
my_car.add_engine(engine)
gearbox = input("Qué tipo de caja de cambios?:")
my_car.add_gearbox(gearbox)

print(my_car)

engine = input("Qué tipo de motor?:")
my_car.add_engine(engine)
print(my_car)