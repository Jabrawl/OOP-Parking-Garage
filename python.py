class Parking_Garage():
    MAX_SPACES = 20
    
    def __init__(self):
        self.user = {}
        self.parkingSpaces = []
        self.currentTicket = {}

    def takeTicket(self):
        if len(self.parkingSpaces) < self.MAX_SPACES:
            current_user = input("What is your name? ").title()
            current_car = input("What is the model of your car: ").title()
            if current_user in self.user and current_user not in self.parkingSpaces:
                self.user[current_user][0] = current_car
                if self.user[current_user][1] == 0:
                    current_bank = int(input("How much money do you have? (In dollars) "))
                    if current_bank < 1:
                        print("Insufficient Funds")
                    else:    
                        self.parkingSpaces.append(current_user)    
                        self.currentTicket[current_user] = False
                else:
                    self.parkingSpaces.append(current_user)    
                    self.currentTicket[current_user] = False
            elif current_user in self.parkingSpaces:
                print("\nYou already have a car parked here! (Only 1 per person) ")
            else:
                current_bank = int(input("How much money do you have? (In dollars) "))
                if current_bank < 1:
                        print("Insufficient Funds")
                else:    
                    self.user[current_user] = [current_car , current_bank]
                    self.parkingSpaces.append(current_user)    
                    self.currentTicket[current_user] = False   
        else:
            print(f"This garage can only hold {self.MAX_SPACES} spaces, please come again later! (We need your money)")
            
    def payForParking(self):
        if len(self.parkingSpaces) > 0:
            while True:               
                for username in self.parkingSpaces:  
                    if self.currentTicket[username] == False:
                        print(f"{username}, {self.user[username][0]} : unpaid")
                    else:
                        print(f"{username}, {self.user[username][0]} : paid")
                paying_for = input("\nWhich user's car would you like to pay for? (Enter 'quit' to go back) ").title()
                if paying_for in self.parkingSpaces and self.currentTicket.get(paying_for) == False:
                    try:
                        card_num = int(input("\nParking Fee: $1\nPlease enter a valid 16-digit credit card number: "))
                        if len(str(card_num)) == 16 and isinstance(card_num, int):
                            self.user[paying_for][1] -= 1
                            self.currentTicket[paying_for] = True
                            print(f"${self.user[paying_for][1]} left in your bank account")
                            print(f"You have succesfully paid for your {self.user[paying_for][0]}, thanks for the money!")
                            break
                        else:
                            print("\nCard Number Invalid")
                    except:
                        print("\nCard Number Invalid")
                elif paying_for in self.parkingSpaces and self.currentTicket.get(paying_for) == True:
                    print(f"{paying_for} has already been paid for, but we will happily take your money!")
                    break
                elif paying_for.lower() in ('no', 'quit', 'n', 'sike'):
                    break
                else:
                    print(f"That car is not in our garage! Try again")   
        else:
            print("This garage is empty, but you can still pay us if you want")
    
    def leaveGarage(self):
        for username in self.parkingSpaces:
            if self.currentTicket[username] == False:
                print(f"{username}, {self.user[username][0]} : unpaid")
            else:
                print(f"{username}, {self.user[username][0]} : paid")
        if len(self.parkingSpaces) > 0:
            while True:
                whos_leaving = input("\nWho is leaving? (Enter 'quit' to go back) ").title()
                if whos_leaving in self.parkingSpaces and self.currentTicket.get(whos_leaving) == True:
                    print(f"Thanks for stopping by! Your {self.user[whos_leaving][0]} is beautiful by the way")
                    self.parkingSpaces.remove(whos_leaving)
                    del self.currentTicket[whos_leaving]
                    break
                elif whos_leaving in self.parkingSpaces and self.currentTicket.get(whos_leaving) == False:
                    leaving = input(f"{whos_leaving}'s {self.user[whos_leaving][0]} has not been paid for yet, pay right now? [y/n] ").lower()
                    if leaving == "y":
                        try:
                            card_num = int(input("\nParking Fee: $1\nPlease enter a valid 16-digit credit card number: "))
                            if len(str(card_num)) == 16 and isinstance(card_num, int):
                                self.user[whos_leaving][1] -= 1
                                self.currentTicket[whos_leaving] = True
                                print(f"${self.user[whos_leaving][1]} left in your bank account")
                                print(f"\nThanks for stopping by! Your {self.user[whos_leaving][0]} is beautiful by the way")
                                self.parkingSpaces.remove(whos_leaving)
                                del self.currentTicket[whos_leaving]
                                break
                            else:
                                print("Card Number Invalid")
                        except:
                            print("Card Number Invalid")    
                    else:
                        break
                elif whos_leaving.lower() in ('no', 'quit', 'n', 'sike'):
                        break
                else:
                    print("That car is not in our garage! Try again")

        else:
            print("This garage is empty, how can you leave?")

    def showGarage(self):
        if len(self.parkingSpaces) > 0:
            for username in self.parkingSpaces:
                if self.currentTicket[username] == False:
                    print(f"{username}, {self.user[username][0]} : unpaid")
                else:
                    print(f"{username}, {self.user[username][0]} : paid")
        else:
            print("There are no cars currently parked here.")

    def userHistory(self):
        if len(self.user) > 0:
            for users in self.user:
                if users in self.parkingSpaces:
                    print(f"User: {users}, Car: {self.user[users][0]}, Remaining balace: ${self.user[users][1]}, Currently parked ")
                else:
                    print(f"User: {users}, Car: {self.user[users][0]}, Remaining balace: ${self.user[users][1]}, Not currently parked ")
        else:
            print("No users have been created yet.")

    def run(self):
        while True:
            user_input = input("""
            Please choose one of the following numbers:
            [1] Parking
            [2] Paying for parking
            [3] Leaving the garage
            [4] Show current garage
            [5] Show User History
            [6] Quit
            """)
            if user_input == "1":
                self.takeTicket()
            elif user_input == "2":    
                self.payForParking()
            elif user_input == "3":
                self.leaveGarage()
            elif user_input == "4":
                self.showGarage()
            elif user_input == "5":
                self.userHistory()
            elif user_input == "6":
                print("Come back again!")
                break
            else:
                print(f"{user_input} is not on this list, please try again")


nissan = Parking_Garage()

nissan.run()