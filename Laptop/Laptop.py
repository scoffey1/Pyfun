class Laptop:
    brand = "Dell" #class attribute
    def __init__(self, ram: str, processor: str):
        self.ram = ram
        self.processor = processor

    @classmethod
    def change_brand(cls, new_brand: str) -> None:
        if new_brand.isalpha() and len(new_brand) <= 10:
            cls.brand = new_brand
        else:
            raise ValueError(f"{new_brand} is not ok!")
        
    
laptop = Laptop("4GB", "Intel I7")
Laptop.change_brand("Apple")
print(laptop.brand)