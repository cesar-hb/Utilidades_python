import random
import sqlite3


account_list = {}
with sqlite3.connect('card.s3db') as conn:  # Context manager for SQLite connection
    cur = conn.cursor()  # Cursor for sqlite3
    cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER DEFAULT 0, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
    conn.commit()


class Bankcard:
    def __init__(self):
        self.bank_id_number = str(400000)
        self.account_identifier = str(random.randint(0, 999999999)).zfill(9)
        self.ready_for_checksum = self.bank_id_number + self.account_identifier
        self.checksum = self.card_checksum(self.ready_for_checksum)
        self.card_number = self.bank_id_number + self.account_identifier + str(self.checksum)
        self.card_pin = str(random.randint(0, 9999)).zfill(4)
        self.balance = 0

    @staticmethod
    def card_checksum(ready_for_checksum):
        card_number = ready_for_checksum
        result = ""
        total_sum = 0
        checksum = 0
        count = 2
        for x in card_number:
            temp = int(x)
            if count % 2 == 0:
                temp = int(x) * 2
                if temp > 9:
                    temp -= 9
            result += str(temp)
            count += 1
        for x in result:
            total_sum += int(x)
        if total_sum % 10 == 0:
            pass
        else:
            checksum = abs(total_sum % 10 - 10)
        return checksum

    @staticmethod
    def menu():
        print("1. Create an account\n2. Log into account\n0. Exit")
        choice = input()
        if choice == "1":
            Bankcard.create_account()
        elif choice == "2":
            Bankcard.auth()

    @staticmethod
    def create_account():
        new_card = Bankcard()
        card_number = new_card.card_number
        card_pin = new_card.card_pin
        with sqlite3.connect('card.s3db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT MAX(id) from card')
            db_result = cur.fetchone()
            last_id = 1
            if db_result[0] is not None:
                last_id = db_result[0] + 1
            cur.execute('INSERT INTO card (id, number, pin) VALUES (' + str(last_id) + ', "' + card_number + '", "' + card_pin + '");')
            # .format truncates trailing zeroes on SQLite database, don't know why
            conn.commit()
        print("Your card has been created\nYour card number:\n{}\nYour card PIN:\n{}\n".format(card_number, card_pin))
        return Bankcard.menu()

    @staticmethod
    def auth():
        print("Enter your card number:")
        c_number = input()
        print("Enter your PIN:")
        c_pin = input()
        with sqlite3.connect('card.s3db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT * from card WHERE number = {} AND pin = {}'.format(c_number, c_pin))
            db_result = cur.fetchone()
            if db_result is not None:
                print("You have successfully logged in!")
                Bankcard.logged_in(c_number)
            else:
                print("Wrong card number or PIN!")
                Bankcard.menu()

    @staticmethod
    def logged_in(c_number):
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
        choice = input()
        if choice == "1":
            with sqlite3.connect('card.s3db') as conn:
                cur = conn.cursor()
                cur.execute(f'SELECT balance FROM card WHERE number = {c_number};')
                balance = cur.fetchone()
                print(f'Balance: {balance[0]}')
            Bankcard.logged_in(c_number)
        elif choice == "2":
            print("Enter income:")
            amount = int(input())
            with sqlite3.connect('card.s3db') as conn:
                cur = conn.cursor()
                cur.execute(f'SELECT balance FROM card WHERE number = {c_number};')
                db_result = cur.fetchone()
                update_balance = db_result[0] + amount
                cur.execute(f'UPDATE card SET balance = {update_balance} WHERE number = {c_number};')
                conn.commit()
            print('Income was added!')
            Bankcard.logged_in(c_number)
        elif choice == "3":
            print('Enter card number:')
            target_account = input()
            target_checksum_digit = int(target_account) % 10  # Modulo 10 gives the last digit of any positive number
            ready_to_check_chesksum = str(target_account).rstrip(target_account[-1]) # c_number without checksum digit
            if target_account == c_number:
                print("You can't transfer money to the same account!")
                Bankcard.logged_in(c_number)
            elif Bankcard.card_checksum(ready_to_check_chesksum) != int(target_checksum_digit):
                print('Probably you made a mistake in the card number.')
                Bankcard.logged_in(c_number)
            else:
                with sqlite3.connect('card.s3db') as conn:
                    cur = conn.cursor()
                    cur.execute(f'SELECT number FROM card WHERE number = {target_account};')
                    target = cur.fetchone()
                    if target is None:
                        print('Such a card does not exist.')
                        Bankcard.logged_in(c_number)
                    else:
                        print('Enter how much money you want to transfer:')
                        amount = int(input())
                        cur.execute(f'SELECT balance FROM card WHERE number = {c_number};')
                        target = cur.fetchone() # Another target, don't know if it can cause conflict with the previous
                        if target[0] < amount:
                            print('Not enough money!')
                            Bankcard.logged_in(c_number)
                        else:
                            update_balance_origin = target[0] - amount
                            cur.execute(f'UPDATE card SET balance = {update_balance_origin} WHERE number = {c_number};')
                            conn.commit()
                            cur.execute(f'SELECT balance FROM card WHERE number = {target_account};')
                            target = cur.fetchone()
                            update_balance_target = target[0] + amount
                            cur.execute(f'UPDATE card SET balance = {update_balance_target} WHERE number = {target_account};')
                            conn.commit()
                            print('Success!')
                            Bankcard.logged_in(c_number)
        elif choice == "4":
            print('The account has been closed!')
            with sqlite3.connect('card.s3db') as conn:
                cur = conn.cursor()
                cur.execute(f'DELETE FROM card WHERE number = {c_number}')
                conn.commit()
                Bankcard.menu()
        elif choice == "5":
            Bankcard.menu()
        else:
            print("Bye!")
            exit()


Bankcard.menu()
