from bank_user import BankUser


class BankAccount:
    def __init__(self, ac_num: str, user: BankUser) -> None:
        self._ac_num = ac_num
        self._balance = 0
        self._is_active = False
        self._user = user

    def set_balance(self, amt: int) -> None:
        self._balance = amt

    def get_balance(self) -> int:
        return self._balance

    def activate_account(self) -> None:
        self._is_active = True

    def de_activate_account(self) -> None:
        self._is_active = False

    def get_ac_num(self):
        return self._ac_num

    def get_acc_active_status(self) -> bool:
        return self._is_active

    def __str__(self) -> str:  # converts state into string representation
        return f'''
         Ac # : {self._ac_num} 
         Balance : {self._balance} 
         Status : {self._is_active}
        '''