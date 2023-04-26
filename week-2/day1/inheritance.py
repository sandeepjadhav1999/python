
class Abc:
    def abc(self):
        print('from abc')
    pass

class badageexception(Exception,Abc):
    def __init__(self,message):
        super().__init__(message)
        self.messsage=message
    def abc(self):
        super().abc()
        print('from bad')
