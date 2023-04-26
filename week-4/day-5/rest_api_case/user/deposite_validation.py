from user.user_exception import *


class DepositValidation:
    def is_valid(self,deposites:dict):
        if (not set(deposites.keys()).issubset(('acc_num_deposit','amt'))):
            raise InvalidUserException('send required keys only')
        try:
            self.is_amount_valid(deposites.get('amt'))
            return True
        except:
            raise

    def is_amount_valid(self,amt:int):
        if(amt<=0):
            raise InvalidAmountException('please enter the proper amount')
        return True

   