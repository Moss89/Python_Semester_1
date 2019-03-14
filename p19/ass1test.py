def run_slot_machine():
    Purse()

import emoji
from random import choice


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

faces = [emoji.emojize(':red_apple:'),
         emoji.emojize(':pear:'),
         emoji.emojize(':tangerine:')]

def change_face():
    return choice(faces)

class Column:

    def __init__(self):
        self.__current_face = change_face()

    def get_current_face(self):
        return self.__current_face

class Slot:
    def __init__(self):
        self.column1 = Column()
        self.column2 = Column()
        self.column3 = Column()
        self.position1 = 0
        self.position2 = 0
        self.position3 = 0
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
        self.position1 = self.column1.get_current_face()
        self.position2 = self.column2.get_current_face()
        self.position3 = self.column3.get_current_face()
        self.show_slot()

    def show_slot(self):
        print(self.position1, " ", self.position2, " ", self.position3)
        self.score_slot()

    def score_slot(self):
        if self.position1 == self.position2 and self.position2 == self.position3:
            mypurse.credit(self.bet*1.5)
            print("You score", self.bet*1.5, "You have:", mypurse.get_balance())
            self.take_bet()

        elif self.position1 == self.position2 or self.position1 == self.position3 or self.position2 == self.position3:
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

mySlot = Slot()

run_slot_machine()