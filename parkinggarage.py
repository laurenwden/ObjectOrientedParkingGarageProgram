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
                    working_ticket = self.Tickets_Available.pop(0)
                    print(f"Your ticket number is {working_ticket}. Thank you, please take your ticket and enter the garage.")
                    self.current_Ticket_D[working_ticket] = True
                    self.parking_Spaces.pop(0)
                    print('Thank you, Have A Nice Day')  
            if response == 'no':
                #working_ticket isn't a list
                working_ticket = self.Tickets_Available.pop(0)
                print(f"Your ticket number is {working_ticket}. Thank you, please take your ticket and enter the garage.")
                self.current_Ticket_D[working_ticket] = False
                self.parking_Spaces.pop(0)
                print(working_ticket)

    #Method to initiate leaving the garage
    def leaveGarage(self):
        
        Ticket_Number = int(input("What is your ticket number?"))
        
        User_Payment = self.current_Ticket_D.get(Ticket_Number)
        
        #type bool
        
        # for Tickets_Taken, payment in self.current_Ticket_D:
        #^^^we don't need all tix taken
        
        if User_Payment == False:
            self.Input_Payment(Ticket_Number)
        del self.current_Ticket_D[Ticket_Number]
        self.Add_to_List(Ticket_Number)    
        print('Thank you, Have A Nice Day')           

    def Input_Payment(self, Ticket_Number):     
        while input("Your total is $10. Please enter payment amount once you have submitted your payment.") != '10':
            print("FEED MEEE IM HUNGRY!")
        self.current_Ticket_D[Ticket_Number] = True
        
    #Method to pay before leaving
    def payForParking(self):
       
        ticket_number = input("What is your ticket number?")
        
        self.Input_Payment(ticket_number)

        print('Thank you, Have A Nice Day')          

    #Adding items back to available tickets and parking spaces        
    def Add_to_List(self, Ticket_Number):
        
        self.Tickets_Available.append(Ticket_Number)
        
        self.parking_Spaces.append("1")

def Run():
        variable = ParkingGarage([1,2,3,4,5,6,7,8,9,10],[1,1,1,1,1,1,1,1,1,1],{})
        while True:
            User_Input = input('What would you like to do? Park, pay or leave?--quit to exit--' )
            if User_Input.lower() == 'park':
                variable.takeTicket()
                
            if User_Input.lower() == 'pay':
                variable.payForParking()
                
            if User_Input.lower() == 'leave':
                variable.leaveGarage()
            if User_Input.lower() == 'quit':
                return
            
                
Run()

