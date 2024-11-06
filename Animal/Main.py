# Example of Inheritance showing better reusability and extensibility in coding approach

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQEEEK!")
# Creating instances of each animal
dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Stuart")

# Using inherited methods
dog.eat()       # Output: Buddy is eating
cat.sleep()     # Output: Whiskers is asleep
mouse.eat()     # Output: Stuart is eating

# Using the overridden speak method for each animal type
dog.speak()     # Output: WOOF!
cat.speak()     # Output: MEOW!
mouse.speak()   # Output: SQEEEK!
