import random


def create_cart_number():
    """Luhn algorithm"""

    card_number = [4, 0, 0, 0, 0, 0]
    for _ in range(9):
        card_number.append(random.randrange(10))
    number = [n for n in card_number]
    for n in range(0, 15, 2):
        number[n] *= 2
    for n in range(15):
        if number[n] > 9:
            number[n] -= 9
    card_number.append(0 if sum(number) % 10 == 0 else 10 - sum(number) % 10)
    return "".join([str(n) for n in card_number])


class Account:
    bank_cards = {}  # dictionary, key = card_number:list[pin, balans]

    def __init__(self):
        self.card_number = None
        self.card_pin = None
        self.balance = 0

    def generation_card(self):
        self.card_number = create_cart_number()
        self.card_pin = ""
        for _ in range(4):
            self.card_pin += str(random.randrange(10))
        print("\nYour card has been created\nYour card number:\n{}\nYour card PIN:\n{}".format(self.card_number, self.card_pin))
        Account.bank_cards[self.card_number] = [self.card_pin, self.balance]

    # def add_account(self):
    #     Account.bank_cards[self.card_number] = [self.card_pin, self.balance]


MENU_PROGRAM = """
1. Create an account
2. Log into account
0. Exit"""

MENU_CARD = """
1. Balance
2. Log out
0. Exit"""


def create_new_account():
    new_account = Account()
    new_account.generation_card()
    # new_account.add_account()


def menu_card(card):
    print(MENU_CARD)
    n = input("Your choice: > ")
    if n == "1":
        print("\nBalance: {}".format(Account.bank_cards[card][1]))
        menu_card(card)
    if n == "2":
        print("\nYou have successfully logged out!")
        menu_account()
    if n == "0":
        print("\nBye!")
    

def log_into_account():
    number = input("\nEnter your card number:\n> ")
    pin = input("Enter your PIN:\n> ")
    if number in Account.bank_cards.keys() and Account.bank_cards[number][0] == pin:
            print("\nYou have successfully logged in!")
            menu_card(number)
    else:
        print("\nWrong card number or PIN!")
        menu_account()


def menu_account():
    print(MENU_PROGRAM)
    choice = input('Your choice: > ')
    if choice == "0":
        print("\nBye!")
        print("\nAll Account in bank:", Account.bank_cards)
    if choice == "1":
        create_new_account()
        menu_account()
    if choice == "2":
        log_into_account()
    

def main():
    menu_account()

# def menu():
#     start = input('\n1. Create an account\n2. Log into account\n0. Exit')

#     if start == '0':
#         print('Bye!')
#     if start == '1':
#         Bank()
#         menu()
#     if start == '2':
#         login()


# def login():
#     _number = input('Enter your card number: ')
#     _pin = input('Enter your PIN: ')
#     if _number in Bank.accounts.keys() and Bank.accounts[_number][0] == _pin:
#         print('You have successfully logged in!')
#         account_menu(_number)
#     else:
#         print('Wrong card number or PIN!')
#         menu()


# def account_menu(_number):
#     action = input('\n1. Balance\n2. Log out\n0. Exit')

#     if action == '2':
#         print('You have successfully logged out')
#         menu()
#     elif action == '1':
#         print(f'Balance: {Bank.accounts[_number][1]}')
#         account_menu(_number)
#     elif action == '0':
#         print('Bye!')