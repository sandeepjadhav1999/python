from types import resolve_bases


class User():
    def __init__(self,ac_num):
        self.ac_num=ac_num

    def show_details(self):
        x='personal details'
        y='ac_num: '+ self.ac_num
        z=int(self.balance)
        s=f'status: {bool(self.status)}'
        result=[x,y,z,s]
        return result


class Bank(User):
    def __init__(self, ac_num):
        super().__init__(ac_num)
        self.balance=0
        self.status=False

    def deposite(self,amount):
        self.amount=int(amount)
        self.balance=self.balance+self.amount
        return self.balance

    def withdraw(self,amount):
        self.amount=int(amount)
        if self.amount>self.balance:
            return self.amount
        else:
            self.balance=self.balance-self.amount
            return self.balance
            
    def Act_status(self,acc_num):
        self.acc_num=str(acc_num)  
        self.status=True 
        return self.status
    def deact(self,acc_num):
        self.acc_num=acc_num
        self.status=False
        return self.status
    
    def view_balance(self):
        return self.balance

pro=Bank('123')
print(pro.deposite(1000))
print(pro.withdraw(100))
print(pro.deposite(1000))
print(pro.view_balance())
print(pro.show_details())
print(pro.Act_status(123))
print(pro.show_details())
