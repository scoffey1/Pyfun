class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  # Setting a default speed

    def accelerate(self, increase):
        self.speed += increase
        print(f"The car is now going at {self.speed} mph.")

    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)  # Speed can't go below 0
        print(f"The car slowed down to {self.speed} mph.")


# Creating a Car object
my_car = Car("Toyota", "Corolla", 2021)

# Displaying the initial state of the car
print("Car Make:", my_car.make)
print("Car Model:", my_car.model)
print("Car Year:", my_car.year)

# Using the car's methods
my_car.accelerate(30)  # Accelerate by 30 mph
my_car.brake(10)  # Brake by 10 mph
