from Vehicle.Vehicle import Vehicle

class Bicycle(Vehicle):
    def __init__(self, colour, number_of_wheels, brand, model, type_of_bike):
        super().__init__(colour, number_of_wheels)
        self.brand = brand
        self.model = model
        self.type_of_bike = type_of_bike

    def __str__(self):
        return f"Bycicle(Colour={self.colour}, Number of wheels={self.number_of_wheels}, Brand={self.brand}, Model={self.model}, Type of bike={self.type_of_bike})"
    
    def start(self):
        print(f"The bycicle {self.brand} {self.model} is ready to go!")

    def stop(self):
        print(f"The bycicle {self.brand} {self.model} has stopped")

    def catalogue(vehicles):
        for vehicle in vehicles:
            print(f"{vehicle.__class__.__name__}: {vehicle}")