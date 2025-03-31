from Num_of_wheels.Car import Car
from Num_of_wheels.Bicycle import Bicycle
from Type_of_vehicle.Motorcycle import Motorcycle
from Type_of_vehicle.Van import Van

def launcher_main():
    vehicles = []

    vehicles.append(Car("Red", 4, 180, 1600))
    vehicles.append(Car("Blue", 4, 200, 1800))
    vehicles.append(Car("White", 4, 190, 1700))
    vehicles.append(Car("Black", 4, 210, 2000))
    vehicles.append(Car("Silver", 4, 220, 2200))

    vehicles.append(Bicycle("Red", 2, "Giant", "Escape 3", "Road"))
    vehicles.append(Bicycle("Blue", 2, "Trek", "FX 1", "Hybrid"))
    vehicles.append(Bicycle("Green", 2, "Cannondale", "Quick 6", "Fitness"))
    vehicles.append(Bicycle("Black", 2, "Specialized", "Sirrus 2.0", "Commuter"))
    vehicles.append(Bicycle("Yellow", 2, "Scott", "Sub Cross 50", "Mountain"))  

    vehicles.append(Motorcycle("Black", 2, "Harley-Davidson", "Street 750", "Cruiser", 120, 749))
    vehicles.append(Motorcycle("Blue", 2, "Yamaha", "MT-07", "Naked", 180, 689))
    vehicles.append(Motorcycle("Green", 2, "Kawasaki", "Ninja 400", "Sport", 190, 399))
    vehicles.append(Motorcycle("Red", 2, "Ducati", "Monster 821", "Naked", 225, 821))
    vehicles.append(Motorcycle("Black", 2, "BMW", "R 1250 GS", "Adventure", 200, 1254))

    vehicles.append(Van("White", 4, 160, 2000, 1000))
    vehicles.append(Van("Silver", 4, 180, 2200, 1200))
    vehicles.append(Van("Blue", 4, 170, 2100, 1100))
    vehicles.append(Van("Black", 4, 190, 2300, 1300))
    vehicles.append(Van("Red", 4, 200, 2500, 1500))

    def catalogue(vehicles):
        for vehicle in vehicles:
            print(f"Class: {vehicle.__class__.__name__}")
            for attribute, value in vehicle.__dict__.items():
                print(f"  {attribute}: {value}")
            print()

    def catalogue(vehicles, number_of_wheels = None):
        if number_of_wheels is not None:
            filtered_vehicles = [vehicle for vehicle in vehicles if vehicle.number_of_wheels == number_of_wheels]
            print(f"There are {len(filtered_vehicles)} vehicles with {number_of_wheels} wheels")
            for vehicle in filtered_vehicles:
                print(f"Class: {vehicle.__class__.__name__}")
                for attribute, value in vehicle.__dict__.items():
                    print(f"  {attribute}: {value}")
                print()
        else:
            for vehicle in vehicles:
                print(f"Class: {vehicle.__class__.__name__}")
                for attribute, value in vehicle.__dict__.items():
                    print(f"  {attribute}: {value}")
                print()

    catalogue(vehicles)