class Employee:
    company = "Apple"
    bonus_amount = 500
    pay_raise = 1.1
    
    def __init__(self,name: str, pay: int, role: str):
        self.name = name
        self.pay = pay
        self.role = role
      
      
    def show_pay_with_bonus(self) ->None:
        print(f"{self.name} is paid {self.pay + Employee.bonus_amount} with bonus")
     
    def increase_annual_pay(self) ->None:
        self.pay *= Employee.pay_raise
      
    @classmethod
    def change_bonus_amount(cls, new_amount) ->None:
        cls.bonus_amount = new_amount
     
    @classmethod
    def change_rise_pct(cls, new_pct) ->None:
        cls.pay_raise = new_pct
        
        
john = Employee("John", 45000, "Software Engineer")
print(john.company)  # Output: Apple
Employee.change_bonus_amount(15000)
Employee.change_rise_pct(1.5)
john.show_pay_with_bonus()
#john.increase_annual_pay
print(john.pay)