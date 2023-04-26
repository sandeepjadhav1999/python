from types import NoneType
from bank import Bank
from users import UserDatabase

class NoneTypeError(Exception):
    def __init__(self,msg) -> None:
        super().__init__(msg)

class AdminMenuOperation:

    def __init__(self, udb: UserDatabase, bank: Bank) -> None:
        self.udb = udb
        self.bank = bank

    def create_bank_account(self):
        print('\n For Creating Bank Account Enter Following Details')
        user_name = input('\n Enter User Name : ')
        password = input('\n Enter Password : ')

        bu = self.udb.create_new_user(user_name=user_name,password=password,role='user')

        ba = self.bank.create_bank_account(user_id=bu.id)
        print('\n --- Account Successfully Created ----')
        print(ba)

    def all_accounts(self):
        for ac in self.bank.all_accounts():
            print(f'{ac._ac_num}\t {ac._balance} \t {ac._is_active}')

    def deposit(self):
        print('\n For Deposit, Enter Following Details')
        ac_num = input('Enter AC Num : ')
        amt = int(input('Enter Amount : '))

        ac=self.error_acc(ac_num)

        if amt <=0 :
            print('Please enter a positive Value')
        else:
            self.bank.deposit(ac, amt)

    def display_balance(self):
        ac_num = input('Enter AC Num : ')
        ac=self.error_acc(ac_num)
        bal = self.bank.check_balance(ac)
        print(f'{ac.get_ac_num()}\t {bal}')

    def withdraw(self):
        print('\n For Withdraw, Enter Following Details')
        ac_num = input('Enter AC Num : ')
        amt = int(input('Enter Amount : '))
        ac=self.error_acc(ac_num)
        self.bank.withdraw(ac, amt)  

    def transfer_money(self):
        print('\nfor tranfer enter the folowing details:')
        ac_num=input('enter your bank acc no.: ')
        amt=int(input('enter the amount to be transferred: '))
        ac=self.error_acc(ac_num)
        ac_num1 = input('Enter AC Num wer the money to be transferred: ')
        ac1=self.error_acc(ac_num1)
        self.bank.transfer_money(ac,ac1, amt)
    
    def activate_acc(self):
        ac_num=input('enter your bank acc no.: ')
        ac=self.error_acc(ac_num)
        self.bank.activate_account(ac)
    def deactivate_acc(self):
        ac_num=input('enter your bank acc no.: ')
        ac=self.error_acc(ac_num)
        self.bank.de_activate_account(ac)


    def error_acc(self,ac_num):
        ac =self.bank.get_ac_by_num(ac_num)
        if ac==None:
            raise NoneTypeError('please enter a valid acc number')
        return ac 


    


