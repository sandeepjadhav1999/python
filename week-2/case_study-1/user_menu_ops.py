from bank import Bank
from users import UserDatabase

class UserMenuOperation:

    def __init__(self, udb: UserDatabase, bank: Bank) -> None:
        self.udb = udb
        self.bank = bank

    def display_balance(self):
        ac_num = input('Enter AC Num : ')
        ac = self.bank.get_ac_by_num(ac_num)
        bal = self.bank.check_balance(ac)
        print(f'{ac.get_ac_num()}\t {bal}')

    def withdraw(self):
        print('\n For Withdraw, Enter Following Details')
        ac_num = input('Enter AC Num : ')
        amt = int(input('Enter Amount : '))

        ac = self.bank.get_ac_by_num(ac_num)

        self.bank.withdraw(ac, amt)
    
    def deposit(self):
        print('\n For Deposit, Enter Following Details')
        ac_num = input('Enter AC Num : ')
        amt = int(input('Enter Amount : '))

        ac = self.bank.get_ac_by_num(ac_num)

        if amt <=0 :
            print('Please enter a positive Value')
        else:
            self.bank.deposit(ac, amt)

    def transfer_money(self):
        print('\nfor tranfer enter the folowing details:')
        ac_num=input('enter your bank acc no.: ')
        amt=int(input('enter the amount to be transferred: '))
        ac = self.bank.get_ac_by_num(ac_num)
        ac_num1 = input('Enter AC Num wer the money to be transferred: ')
        ac1 = self.bank.get_ac_by_num(ac_num1)
        self.bank.transfer_money(ac,ac1, amt)