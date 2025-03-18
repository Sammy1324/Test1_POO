from Num_of_wheels.Car import Car

class Van(Car):
    def __init__(self, colour, number_of_wheels, speed, displacement, load_capacity):
        super().__init__(colour, number_of_wheels, speed, displacement, load_capacity)
    def __str__(self):
        return f"Van({self.colour}, {self.number_of_wheels}, {self.speed}, {self.displacement}, {self.load_capacity})"
    def load(self):
        print(f"The Van is loading {self.load_capacity} kg of goods")
    def unload(self):
        print(f"The Van is unloading {self.load_capacity} kg of goods")
    def start(self):
        print(f"The Van is ready to go!")
    def stop(self):
        print(f"The Van has stopped")
    def catalogue(vehicles):
        for vehicle in vehicles:
            print(f"{vehicle.__class__.__name__}: {vehicle}")