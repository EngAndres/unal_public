class Engine:
    """This class represents the behavior of an engine in the game."""

    # constructor
    def __init__(self, brand: str, cc: int):
        self.brand = brand
        self.cc = cc
    
    def start(self):
        """This method starts the engine."""
        print('Ruuun')
    
    def stop(self):
        """This method stops and turns off the engine."""
        print('Shshshsh')

# ======================================

class Sticker:
    """This class represents the behavior of a sticker in the car game."""

    def __init__(self, text: str, color: str):
        self.text = text
        self.color = color
