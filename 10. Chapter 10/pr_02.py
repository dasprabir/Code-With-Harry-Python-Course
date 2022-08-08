class Calculator:
    def __init__(self,num) :
        self.number = num

    def sqare(self) :
        print(f"The sqare of the {self.number} is {self.number**2}")

    def sqareRoot(self) :
        print(f"The sqare of the {self.number} is {self.number**0.5}")

    def cube(self) :
        print(f"The sqare of the {self.number} is {self.number**3}")

a = Calculator(9)
a.sqare()
a.sqareRoot()
a.cube()
