class Vehicle:
    def __init__(self, colour, number_of_wheels):
        self.colour = colour
        self.number_of_wheels = number_of_wheels
    
    def __str__(self):
        return "Colour {}, {} wheels".format(self.colour, self.number_of_wheels)
    
    def __name__(self):
        return self.__class__.__name__
    
    def catalogue(vehicles):
        for vehicle in vehicles:
            print(type(vehicle).__name__, vehicle)