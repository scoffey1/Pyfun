from datetime import datetime

class Person:
   
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Return an instance of Person with their age calculated"""
        current_year = datetime.now().year 
        #current_year = 2025
        return cls(name, current_year - birth_year)
    
john = Person("John", 24) # --> init
new_person = Person.from_birth_year("Mary", 1984) # --> class methods --> init
print(vars(new_person))
