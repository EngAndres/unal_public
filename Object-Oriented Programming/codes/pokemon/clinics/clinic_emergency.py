from i_clinic import  Clinic

class ClinicEmergency(Clinic):
    """This class represents the behavior of an emergency clinic,
    it means, some services are limited."""

    def __init__(self, nurse):
        self.nurse = nurse

    def recovery(self, pokemon_type: str) -> int:
        recovery_value = 5
        if(pokemon_type == "water"):
            recovery_value = 8
        elif(pokemon_type == "rock"):
            recovery_value = 3
        return recovery_value
    
    def vacunate(self, pokemon_age: int) -> bool:
        return True if pokemon_age < 2 else False
