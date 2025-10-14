from associations import Engine, Sticker

class Car:
    """
    This class represents the behavior of a Car as the main
    component of the video game.
    """

    def __init__(self, engine: Engine):
        self.engine = engine
        self.stickers = []   

    def add_sticker(self, sticker: Sticker):
        self.stickers.append( sticker )
    
    def print_car(self):
        print(f'I have an engine: Brand->{self.engine.brand}')
        if len(self.stickers) > 0:
            for s in self.stickers:
                print(s.text)
        else:
            print("No stickers")
            