from user.user_exception import *


class WithdrawValidation:
    def is_valid(self,withdraw:dict):
        if (not set(withdraw.keys()).issubset(('acc_num_withdraw','amt'))):
            raise InvalidUserException('send required keys only')
        try:
            self.is_amount_valid(withdraw.get('amt'))
            return True
        except:
            raise

    def is_amount_valid(self,amt:int):
        if(amt<=0):
            raise InvalidAmountException('please enter the proper amount')
        return True