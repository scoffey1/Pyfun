from random import randint

class Cheese:
    def __init__(self, strength):
        self.strength = strength
        
    @classmethod
    def weak_cheese(cls):
        """Return an instance of cheese with strength 1-4"""
        return cls(randint(1, 4))
    
    @classmethod
    def strong_cheese(cls):
        """Return an instance of cheese with strength 7-10"""
        return cls(randint(7, 10))
    
weak = Cheese.weak_cheese()
print(weak.strength)  # prints a random number between 1 and 4

strong = Cheese.strong_cheese()
print(strong.strength)  # prints a random number between 7 and 10