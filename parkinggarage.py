class ParkingGarage():
    def __init__(self, tickets, parking_Spaces, current_Ticket):
        self.tickets = tickets
        self.parking_Spaces = parking_Spaces
        self.current_Ticket = current_Ticket  #{ticket_number:paid = T or F}
        #self.current_ticket[ticket_number] = True

    # def Parking(self, parking_Spaces):
    #     self.parking_Spaces= list()
    #     print(self.parking_Spaces)
    
    # def Add_Ticket(self, tickets):
    #     Tickets = input('Would you like to purchase a ticket? ')
    #     selfTicket):.tickets.append(Tickets)

    # def Pay(self, current_
    #     pay = input('Have A Nice Day')

    
    def takeTicket():
        if len(parking_spaces) == 0:
            print("I'm sorry, there are no available spaces! Have a nice day.")
            break    
        else:
            payment = input("Would you like to pay now? Enter yes or no")
            if payment == 'yes':
                self.parking_Spaces.pop([0])
                self.tickets.pop([0])   
                self.current_ticket[tickets.popped([0])] = True
            if payment == 'no':
                self.parking_Spaces.pop([0])
                self.tickets.pop([0])
                self.current_ticket[tickets.popped([0])] = False
                print("Please take your ticket.")
            




    def Pay(self, current_
        #change dictionary paid value from false to true
        leaveGarage()
        pay = input('Have A Nice Day')


    def leaveGarage(self, tickets, parking_Spaces, current_Ticket):
        #if they haven't paid they need to pay
            # refer to current_ticket dictionary 
            Pay()

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
Run()
