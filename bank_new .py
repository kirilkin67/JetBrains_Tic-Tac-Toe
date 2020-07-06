import random
import sqlite3


MENU_PROGRAM = """
1. Create an account
2. Log into account
0. Exit"""


MENU_CARD = """
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit"""


class Account:
    # bank_card = []  # list(id, number, pin, balans)

    def __init__(self, file_name, number):
        conn = sqlite3.connect(file_name)
        cur = conn.cursor()
        num_card = [number]
        account = cur.execute("SELECT id, number, pin, balance FROM card WHERE number = ?", num_card)
        self.id = account[0]
        self.card_number = account[1]
        self.card_pin = account[2]
        self.balance = account[3]
        conn.commit()
        conn.close()


    def log_into_account():
        number = input("\nEnter your card number:\n> ")
        pin = input("Enter your PIN:\n> ")
        if number == Account.self.card_number and Account.self.card_pin == pin:
            print("\nYou have successfully logged in!")
            menu_card(number)
        else:
            print("\nWrong card number or PIN!")
            menu_account()


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


def menu_account():
    print(MENU_PROGRAM)
    choice = input('Your choice: > ')
    if choice == "0":
        print("\nBye!")
        print("\nAll Account in bank:", Account.bank_cards)
    if choice == "1":
        create_account()
        menu_account()
    if choice == "2":
        Account.log_into_account()


def create_card_number():
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


def generation_number(digit):
    number = ""
    for _ in range(digit):
        number += str(random.randrange(10))
    return number


def create_database(file_name):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS card (
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0)""")
    conn.commit()
    conn.close()


def create_account(file_name):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    id_a = generation_number(6)
    card = create_card_number()
    pin = generation_number(4)
    account = [id_a, card, pin, 0]
    cur.execute("INSERT INTO card VALUES (?, ?, ?, ?)", account)
    print("\nYour card has been created\n"
          "Your card number:\n{}\n"
          "Your card PIN:\n{}".format(card, pin))
    conn.commit()
    conn.close()
    

def select_database(file_name):
    conn = sqlite3.connect(file_name)
    cur = conn.cursor()
    cur.execute('SELECT id, number, pin, balance FROM card')
    account = cur.fetchall()
    conn.commit()
    conn.close()
    return account


def print_database(file_name):
    accounts = select_database(file_name)
    for account in accounts:
        print(account)

def main():
    database_card = 'card.s3db'
    create_database(database_card)
    print_database(database_card, end='\n')
    menu_account()
    # create_account(database_card)
    # insert_database(db_card)
    # update_database(database_card)
    # select_database(database_card)
    