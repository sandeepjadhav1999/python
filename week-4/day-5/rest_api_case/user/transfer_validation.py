from user.user_exception import *


class TransferValidation:
    def is_valid(self,transfer:dict):
        if (not set(transfer.keys()).issubset(('src_acc','tar_acc','amt'))):
            raise InvalidUserException('send required keys only')
        try:
            self.is_amount_valid(transfer.get('amt'))
            return True
        except:
            raise

    def is_amount_valid(self,amt:int):
        if(amt<=0):
            raise InvalidAmountException('please enter the proper amount')
        return True