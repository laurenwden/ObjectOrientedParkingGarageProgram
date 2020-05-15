class ParkingGarage():
    def __init__(self, Tickets_Available, parking_Spaces, current_Ticket_D):
        self.Tickets_Available = Tickets_Available
        self.parking_Spaces = parking_Spaces
        self.current_Ticket_D = current_Ticket_D  

                
    # Method for taking a ticket to enter the garage        
    def takeTicket(self):
        if len(self.parking_Spaces) == 0:
            print("I'm sorry, there are no available spaces! Have a nice day.")
            return
        else:            
            response = input("Would you like to pay now? Type yes for now or no for later.")
            if response == 'yes':
                payment = input("Your total is $10. Please enter payment amount once you have submitted your payment.")
                if payment == '10':
                    working_ticket = []
                    working_ticket.append(self.Tickets_Available[0])
                    self.current_Ticket_D[working_ticket] = True
                    self.parking_Spaces.pop(0)
                    self.Tickets_Available.pop(0)
                    print("Thank you, please take your ticket and enter the garage.")
            if response == 'no':
                working_ticket = []
                working_ticket.append(self.Tickets_Available[0])
                self.current_Ticket_D[working_ticket] = False
                self.parking_Spaces.pop(0)
                self.Tickets_Available.pop(0)
                print("Thank you, please take your ticket and enter the garage.")
                
    
    #Method for entering the garage after taking ticket/payment          
    def enterGarage(self):
        working_ticket = []
        working_ticket.append(self.Tickets_Available[0])
        self.current_Ticket_D[working_ticket] = True
        self.parking_Spaces.pop(0)
        self.Tickets_Available.pop(0)    
        print("Thank you, please take your ticket and enter the garage.")

      

    #Method to initiate leaving the garage
    def leaveGarage(self):
        Tickets_Taken = input("What is your ticket number?")
        self.current_Ticket_D.get(Tickets_Taken)
        for Tickets_Taken, payment in self.current_Ticket_D:
            if payment == True:
                self.add_to_list()
                print('Thank you, have a nice day!')
            else:
                self.pay
                self.add_to_list()
    
    #Method to pay before leaving
    def pay(self):
        for Tickets_Taken, payment in self.current_Ticket_D:
            self.current_Ticket_D[Tickets_Taken] = True
            del self.current_Ticket_D[Tickets_Taken]
            print('Thank you, Have A Nice Day')           
            

    #Adding items back to available tickets and parking spaces        
    def add_to_list(self):
        self.Tickets_Available.append(Tickets_Taken)
        self.parking_Spaces.append("1")
    
    
               
            

def Run():
        variable = ParkingGarage([1,2,3,4,5,6,7,8,9,10],[1,1,1,1,1,1,1,1,1,1],{})
        while True:
            User_Input = input('What would you like to do? Park, pay or leave?' )
            if User_Input.lower() == 'park':
                variable.takeTicket()
                break
            if User_Input.lower() == 'pay':
                variable.pay()
                break
            if User_Input.lower() == 'leave':
                variable.leaveGarage()
                break
            return
Run()
