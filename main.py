from Num_of_wheels.Car import Car
from Num_of_wheels.Bicycle import Bicycle
from Type_of_vehicle.Motorcycle import Motorcycle
from Type_of_vehicle.Van import Van
from launcher import launcher_main, catalogue

def menu():
    print("Select vehicle")
    print("1. Car")
    print("2. Bicycle")
    print("3. Motorcycle")
    print("4. Van")
    print("5. Sort by number of wheels")
    print("6. Exit")

def get_data(type_of_vehicle):
    if type_of_vehicle == 1:
        colour = input("Enter the colour of the car: ")
        number_of_wheels = int(input("Enter the number of wheels of the car: "))
        speed = int(input("Enter the speed of the car: "))
        displacement = int(input("Enter the displacement of the car: "))
        return Car(colour, number_of_wheels, speed, displacement)
    elif type_of_vehicle == 2:
        colour = input("Enter the colour of the bicycle: ")
        number_of_wheels = int(input("Enter the number of wheels of the bicycle: "))
        brand = input("Enter the brand of the bicycle: ")
        model = input("Enter the model of the bicycle: ")
        type_of_bike = input("Enter the type of bike: ")
        return Bicycle(colour, number_of_wheels, brand, model, type_of_bike)
    elif type_of_vehicle == 3:
        colour = input("Enter the colour of the motorcycle: ")
        number_of_wheels = int(input("Enter the number of wheels of the motorcycle: "))
        brand = input("Enter the brand of the motorcycle: ")
        model = input("Enter the model of the motorcycle: ")
        type_of_bike = input("Enter the type of bike: ")
        displacement = int(input("Enter the displacement of the motorcycle: "))
        speed = int(input("Enter the speed of the motorcycle: "))
        return Motorcycle(colour, number_of_wheels, brand, model, type_of_bike, displacement, speed)
    elif type_of_vehicle == 4:
        colour = input("Enter the colour of the van: ")
        number_of_wheels = int(input("Enter the number of wheels of the van: "))
        speed = int(input("Enter the speed of the van: "))
        displacement = int(input("Enter the displacement of the van: "))
        load_capacity = int(input("Enter the load capacity of the van: "))
        return Van(colour, number_of_wheels, speed, displacement, load_capacity)
    elif type_of_vehicle == 5:
        number_of_wheels = int(input("Enter the number of wheels: "))
        catalogue(vehicles = [], number_of_wheels = number_of_wheels)
        return None
    else:
        return None
    
if __name__ == "__main__":
    while True:
        menu()
        option = int(input("Enter an option: "))
        if option == 6:
            break
        vehicle = get_data(option)
        if vehicle:
            print(f"Created vehicle: {vehicle}")
        else:
            print("Unknown option")
    launcher_main()