class Train :
    def __init__(self,name,fare,seats) :
        self.name = name 
        self.fare = fare 
        self.seats = seats 

    def getStatus(self) :
        print(f"The name of the train is {self.name}")
        print(f"The seats available  in  the train is {self.seats}")

    def getFairInfo(self) :
        print(f"The fair of the train is : Rs {self.fare}")

    def bookTicket(self):
        if (self.seats > 0) :
            print(f"Your ticket has been booked! and your seat number is {self.seats}")
            self.seats = self.seats - 1
        else :
            print("Sorry ! Seats are full!!!")
    def cancelTicket(self) :
        pass


        
intercity = Train("Intercity Express", 90,2)
intercity.getStatus()
#intercity.getFairInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()

intercity.getStatus()


