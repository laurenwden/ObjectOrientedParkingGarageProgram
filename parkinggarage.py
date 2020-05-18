class ParkingGarage():
    def __init__(self, tickets_available, parking_spaces, current_ticket_d):
        self.tickets_available = tickets_available
        self.parking_spaces = parking_spaces
        self.current_ticket_d = current_ticket_d

    # Method for taking a ticket to enter the garage
    def takeTicket(self):
        if len(self.parking_spaces) == 0:
            print("\nI'm sorry, there are no available spaces! Have a nice day.")
            return
        else:
            response = input(
                "\nWould you like to pay now? Type yes for now or no for later.")

            if response == 'yes':
                payment = input("\nYour total is $10. Please enter payment amount once you have submitted your payment.")

                if payment == '10':
                    working_ticket = self.tickets_available.pop(0)
                    print(
                        f"\nYour ticket number is {working_ticket}. Thank you, please take your ticket and enter the garage.")
                    self.current_ticket_d[working_ticket] = True
                    self.parking_spaces.pop(0)
                else:
                    payment = input(
                        "\nYour total is $10. Please enter payment amount once you have submitted your payment.")

                    working_ticket = self.tickets_available.pop(0)

                    print(
                        f"\nYour ticket number is {working_ticket}. Thank you, please take your ticket and enter the garage.")

                    self.current_ticket_d[working_ticket] = True
                    self.parking_spaces.pop(0)
            if response == 'no':
                working_ticket = self.tickets_available.pop(0)
                print(f"\nYour ticket number is {working_ticket}. Thank you, please take your ticket and enter the garage.")
                self.current_ticket_d[working_ticket] = False
                self.parking_spaces.pop(0)

        #Method to pay before leaving
    def payForParking(self):
        ticket_number = int(input("\nPlease enter your ticket number."))
        if ticket_number in self.current_ticket_d:
            if self.current_ticket_d[ticket_number] == True:
                print("\nYou have already paid.")
            else:
                payment = input(
                    "\nYour total is $10. Please enter amount once you have submitted your payment.")

                if payment != '10':
                    print("\nThat is not the correct amount.")
                else:
                    self.current_ticket_d[ticket_number] = True
                    self.tickets_available.append(ticket_number)
                    self.parking_spaces.append(1)
                    print(
                        '\nThank you! You have 15 minutes to leave the garage. Have a nice day!')
        else:
            print("\nThat is not a valid ticket number.")

    #Method to initiate leaving the garage
    def leaveGarage(self):
        ticket_number = int(input("\nWhat is your ticket number?"))

        if ticket_number in self.current_ticket_d:       
            payment = self.current_ticket_d.get(ticket_number)

            if payment == False:
                print("\nYou must pay before exiting.")
            else:
                del self.current_ticket_d[ticket_number]
                self.tickets_available.append(ticket_number)
                self.parking_spaces.append(1)
                print('Thank you! You have 15 minutes to leave the garage. Have a nice day!')

        else:
            print("\nThat is not a valid ticket number.")

def Run():
        action = ParkingGarage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [
                                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], {})

        while True:
            user_input = input('What would you like to do? Park, pay or leave?')
            if user_input.lower() == 'park':
                action.takeTicket()
            if user_input.lower() == 'pay':
                action.payForParking()
            if user_input.lower() == 'leave':
                action.leaveGarage()           
                
Run()

