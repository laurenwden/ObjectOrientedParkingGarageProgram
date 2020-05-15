class ParkingGarage():
    def __init__(self, Tickets_Available, parking_Spaces, current_Ticket_D):
        self.Tickets_Available = Tickets_Available
        self.parking_Spaces = parking_Spaces
        self.current_Ticket_D = current_Ticket_D  

    
    def paynow(self, Tickets_Available, parking_Spaces, current_Ticket, Tickets_Taken):
        payment = input("Would you like to pay now? Enter yes or no")
        if payment == 'yes':
                self.parking_Spaces.pop([0])
                self.Tickets_Available.pop([0])   
                self.Tickets_Taken[Tickets_Available.popped([0])] = True
                
        if payment == 'no':
            self.parking_Spaces.pop([0])
            self.Tickets_Available.pop([0])
            self.current_Ticket_D[Tickets_Available.popped([0])] = False
            print("Please take your ticket.")
            
            
    def takeTicket(self):
        if len(self.parking_Spaces) == 0:
            print("I'm sorry, there are no available spaces! Have a nice day.")
            return
        else:
            
            paynow() 
            
    def Pay(self, current_Ticket_D):
        #change dictionary paid value from false to true
        Tickets_Taken[Value] = True
        del Tickets_Taken[Value]
        Value
        pay = input('Have A Nice Day')


    def leaveGarage(self, Tickets_Available, parking_Spaces, current_Ticket_D):
        #if they haven't paid they need to pay
            # refer to current_ticket dictionary 
            
            for Tickets_Taken, Values in current_Ticket_D.items():
                print(key,values)
                if payment == True:
                    print('Thank you, have a nice day!')
                else:
                    Pay()
    def Add_To_List(self,  Tickets_Available, parking_Spaces):
        Tickets_Available.append(Tickets_Taken)
        parking_Spaces.append("space available")
    
    
               
            

def Run():
        variable = ParkingGarage([1,2,3,4,5,6,7,8,9,10],[1,1,1,1,1,1,1,1,1,1],{})
        while True:
            User_Input = input('What would you like to do? Park, pay or leave?' )
            if User_Input.lower() == 'park':
                variable.takeTicket()
                break
            if User_Input.lower() == 'pay':
                variable.Pay()
                break
            if User_Input.lower() == 'leave':
                variable.leaveGarage()
                break
            return
Run()
        