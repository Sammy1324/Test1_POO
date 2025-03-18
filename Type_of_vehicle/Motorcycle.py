from Num_of_wheels.Bicycle import Bicycle

class Motorcycle(Bicycle):
    def __init__(self, colour, number_of_wheels, brand, model, type_of_bike, displacement, speed):
        super().__init__(colour, number_of_wheels, brand, model, type_of_bike)
        self.displacement = displacement
        self.speed = speed
    def __str__(self):
        return f"Motorcycle({self.colour}, {self.number_of_wheels}, {self.displacement}, {self.speed})"
    
    def catalogue(vehicles):
        for vehicle in vehicles:
            print(f"{vehicle.__class__.__name__}: {vehicle}")

    def start(self):
        print(f"The motorcycle {self.brand} {self.model} is starting")