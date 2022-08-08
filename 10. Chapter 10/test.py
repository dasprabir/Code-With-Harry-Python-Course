class Programmer :
    company = "Microsoft"
    def __init__(self,name,product) : #Constructor
        self.name = name
        self.product = product

    def getInfo(self) :
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

    @staticmethod
    def greet() :
        print("Welcome to the world of coding!!!")
    
    
harry = Programmer("Harry","Skype")
alka = Programmer("Alka","Github")

harry.getInfo()
alka.getInfo()
harry.greet()

