from Vehicle.Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, colour, number_of_wheels, displacement, speed):
        super().__init__(colour, number_of_wheels)
        self.displacement = displacement
        self.speed = speed

    def __str__(self):
        return f"Car({self.colour}, {self.number_of_wheels}, {self.displacement}, {self.speed})"

    def catalogue(vehicles):
        for vehicle in vehicles:
            print(f"{vehicle.__class__.__name__}: {vehicle}")