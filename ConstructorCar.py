# Constructor Car Class
# 2 attributes
# method to change color
# method to write details to text file
class Car:
    """A template to resemble a car""" #Docstring
    def __init__(self, color: str, power: str):
        self.color = color.title() #formatting
        self.power = power
        
    def change_color(self, new_color: str): # change the color of the car
        self.color = new_color

    def write_to_text(self) -> None:
        """Write details to text file"""
        write_string = f"Color: {self.color}, Power: {self.power}\n"
        print(write_string)
        with open("car_details.txt", mode="a") as file:
            file.write(write_string)
        print("Written to file.")
            
car_a = Car("Red","650HP")
car_a.change_color("Blue")
car_a.write_to_text()
print(vars(car_a))
