'''
Holds the data and performs the bank operations, 
which are mentioned as features.
'''

from typing import List
from bank_account import BankAccount
from users import UserDatabase
import string
import random


class Bank:

    def __init__(self) -> None:
        self._accounts = []
        self.udb = UserDatabase()

    def create_bank_account(self, **kwargs) -> BankAccount:
        user_id = kwargs.get('user_id')
        ac_num = self.generate_account_number()
        # this code is written just to show you next operation
        ac = self.udb.get_user_by_id(user_id)

        ba: BankAccount = BankAccount(ac_num, ac)
        self._accounts.append(ba)
        return ba

    def check_balance(self,source: BankAccount) -> int: 
        for ac in self._accounts:
            if(ac.get_ac_num() == source.get_ac_num() ) :
                if source.get_acc_active_status() == True:
                    bal = ac.get_balance() 
                    break
                else:
                    print('please activate you acc')
        return bal

    def transfer_money(self,source: BankAccount,target: BankAccount,amt: int) -> bool:
        for ac in self._accounts:
            if(ac.get_ac_num() == source.get_ac_num()):
                if source.get_acc_active_status() == True:
                    if amt <= ac.get_balance():
                        ac.set_balance(ac.get_balance() - amt)
                        for ac1 in self._accounts:
                            if(ac1.get_ac_num() == target.get_ac_num()):
                                if target.get_acc_active_status() == True:
                                    ac1.set_balance(ac1.get_balance() + amt)
                                    print(f'{amt} has been with drawn from Account: {source.get_ac_num()}\t, Avaliable Balance: {source.get_balance()} ')
                            break
                        break
                    else:
                        print(f'Insufficent Balance')
                        break
                else:
                    print('activate your acc')
                    
                                                    
    def withdraw( self,source: BankAccount,amt: int) -> int:
        for ac in self._accounts:
            if(ac.get_ac_num() == source.get_ac_num()):
                if source.get_acc_active_status() == True:
                    if amt <= ac.get_balance():
                        ac.set_balance(ac.get_balance() - amt)
                        print(f'{amt} has been with drawn from Account: {source.get_ac_num()}\t, Avaliable Balance: {source.get_balance()} ')
                        break
                    else:
                        print(f'Insufficent Balance')
                        break
                else:
                    print('plese active you acc')
    def deposit(
        self,
        source: BankAccount,
        amt: int
    ) -> int:
        for ac in self._accounts:
            if(ac.get_ac_num() == source.get_ac_num()):
                if source.get_acc_active_status() == True:
                    ac.set_balance(ac.get_balance() + amt)
                    break
                else:
                    print('acrtivate your acc')
        

    def activate_account(self,source: BankAccount):
        for ac in self._accounts:
            if(ac.get_ac_num() == source.get_ac_num()):
                ac.activate_account()
                print('acc has been activated')

    def de_activate_account(source: BankAccount):
        for ac in self._accounts:
            if(ac.get_ac_num() == source.get_ac_num()):
                ac.de_activate_account()
                print('acc has been deactivated')


    def generate_account_number(self) -> str:
        return ''.join(
            random.choices(
                string.ascii_uppercase + string.digits, k=16
            )
        )

    def all_accounts(self) -> List[BankAccount]:
        return self._accounts

    def get_ac_by_num(self, ac_num: str) -> BankAccount:
        return next((ac for ac in self._accounts if ac_num == ac.get_ac_num()), None)
