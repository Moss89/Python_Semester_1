import emoji
from random import choice

faces = [emoji.emojize(':red_apple:'),
         emoji.emojize(':pear:'),
         emoji.emojize(':tangerine:')
         ]

class Purse:
        def __init__(self):
            self.__money = 10

        def debit(self, amount):
            self.__money -= amount

        def credit(self, amount):
            self.__money += amount

        def get_balance(self):
            return self.__money
mypurse = Purse()

class Column:
        def __init__(self):
            self.face = ""

        def change_face(self):
            self.face = choice(faces)

        def get_face(self):
            return self.face


class Slot:
        def __init__(self):
            self.column1 = Column()
            self.column2 = Column()
            self.column3 = Column()
            self.bet = 0
            self.take_bet()

        def take_bet(self):
            self.bet = input("How much do you bet? ")
            if self.bet == "N":
                print("Thanks for playing!")

            if self.bet != "N":
                try:
                    self.bet = int(self.bet)
                except ValueError:
                    self.take_bet()

                if self.bet < 2:
                    print("Minimum bet is 2!")
                    self.take_bet()

                elif self.bet > mypurse.get_balance():
                    print("You don't have enough money to make that bet! You only have:", mypurse.get_balance())
                    self.take_bet()
                else:
                    self.pull_handle()

        def pull_handle(self):
            self.column1.change_face()
            self.column2.change_face()
            self.column3.change_face()
            self.show_slot()

        def show_slot(self):
            print(self.column1.get_face(), " ", self.column2.get_face(), " ", self.column3.get_face())
            self.score_slot()

        def score_slot(self):
            if self.column1.get_face() == self.column2.get_face() and self.column2.get_face() == self.column3.get_face():
                mypurse.credit(self.bet*1.5)
                print("You score", self.bet*1.5, "You have:", mypurse.get_balance())
                self.take_bet()

            elif self.column1.get_face() == self.column2.get_face() or self.column1.get_face() == self.column3.get_face() or self.column2.get_face() == self.column3.get_face():
                mypurse.credit(self.bet)
                print("You score", self.bet, "You have:", mypurse.get_balance())
                self.take_bet()

            else:
                mypurse.debit(self.bet)
                print("You score", 0, "You have:", mypurse.get_balance())
                if mypurse.get_balance() < 2:
                    print("You don't have enough money for another bet! You have", mypurse.get_balance(), "Thanks for playing!")
                else:
                    self.take_bet()


def run_slot_machine():
        mySlot = Slot()


run_slot_machine()
