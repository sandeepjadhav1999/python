from user.user_exception import *


class ActivateValidation:
    def is_valid(self,users:dict):
        if (not set(users.keys()).issubset(('ac_num','ac_sts'))):
            raise InvalidUserException('send required keys only')
        try:
            self.is_status_valid(users.get('ac_sts'))
            return True
        except:
            raise

    def is_status_valid(self,ac_sts:int):
        if(ac_sts not in [0,1]):
            raise InvalidStatusException('please enter correct status code')
        return True