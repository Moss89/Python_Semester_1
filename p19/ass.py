import emoji
from random import choice
import sys
def run_slot_machine():

    class Purse:
        def __init__(self):
            self.money = 10

        def debit(self, amount):
            print(amount,"this")
            self.money -= amount

        def credit(self, amount):
            self.money += amount

        def get_balance(self):
            return self.money

    mypurse = Purse()

    class Column:
        def __init__(self):
            self.faces = [emoji.emojize(':red_apple:'),
                          emoji.emojize(':pear:'),
                          emoji.emojize(':tangerine:')
                          ]
        def change_face(self):
            return choice(self.faces)


    class Slot:
        def __init__(self):
            self.column1 = Column()
            self.column2 = Column()
            self.column3 = Column()
            self.position1 = 0
            self.position2 = 0
            self.position3 = 0
            self.bet = 0.0

        def bet_amount(self, amount):
            self.bet = amount

        def get_bet(self):
            return self.bet

        #                 def take_bet(self):
        #                     self.bet = input("How much do you bet? ")
        #                     if self.bet == "N":
        #                         print("Thanks for playing!")
        #                         return False

        #                     if self.bet != "N":
        #                         self.bet = float(self.bet)
        #                         print(self.bet)

        #                         if self.bet<2:
        #                             print("Minimum bet is 2!")
        #                             return True

        #                         elif self.bet > mypurse.get_balance():
        #                             print("You don't have enough money to make that bet! You only have:", mypurse.get_balance())
        #                             return True
        #                         else:
        #                             return True

        def pull_handle(self):
            self.position1 = self.column1.change_face()
            self.position2 = self.column2.change_face()
            self.position3 = self.column3.change_face()

        def show_slot(self):
            print(self.position1, " ", self.position2, " ", self.position3)

        def score_slot(self, bet):
            if self.position1 == self.position2 and self.position2 == self.position3:
                mypurse.credit(bet*1.5)
                print("You score", bet*1.5, "You have:", mypurse.get_balance())

            elif self.position1 == self.position2 or self.position1 == self.position3 or self.position2 == self.position3:
                mypurse.credit(bet)
                print("You score", bet, "You have:", mypurse.get_balance())

            else:
                mypurse.debit(bet)
                print("You score", 0, "You have:", mypurse.get_balance())
                if mypurse.get_balance() < 2:
                    print("You don't have enough money for another bet! You have", mypurse.get_balance(), "Thanks for playing!")
                    sys.exit()


    mySlot = Slot()
    def take_bet():
        bet = input("How much do you bet? ")
        if bet == "N":
            print("Thanks for playing!")
            result = "Exit"

        if bet != "N":
            bet = float(bet)
            mySlot.bet_amount(bet)
            print("1")

            if bet < 2:
                print("2")
                print("Minimum bet is 2!")
                result = "Retry"

            elif bet > mypurse.get_balance():
                print("3")
                print("You don't have enough money to make that bet! You only have:", mypurse.get_balance())
                result = "Retry"
            else:
                result = "True"

            # #     mySlot.take_bet()

            if result == "Retry":
                print("loop1")
                take_bet()


            if result == "True":
                print("loop2")
                #     mySlot.take_bet()
                mySlot.pull_handle()
                mySlot.show_slot()
                mySlot.score_slot(mySlot.get_bet())
                take_bet()


            if result == "Exit":
                print("Exit loop")
                sys.exit()
    take_bet()
run_slot_machine()

