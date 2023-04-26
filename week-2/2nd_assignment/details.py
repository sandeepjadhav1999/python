import datetime
class st_name:
    def __init__(self):
        self.name=str(input('enter the name:'))
        self.st_names()
    def st_names(self):
        if (len(self.name)>8):
            print('---------------your name is :',self.name,'---------------')
        else:
            print('----------------enter proper name-----------')
class st_salary:
    def __init__(self):
        self.salary=(float(input('enter the salary:')))
        self.st_salarys()
    def st_salarys(self):
        if self.salary>=15000 and self.salary<=2500000:
            print('-----------------your salary is ',self.salary,'---------------')
        else:
            print('----------------please enter the proper salary------------')
class  st_date:
    def __init__(self):
        self.dates=int(input('enter the date:'))
        self.month=int(input('enter the month:'))
        self.year=int(input('enter the year:'))
        self.agesyear=0
        self.st_date()
    def st_date(self):
        self.dob=datetime.datetime(self.year,self.month,self.dates)
        self.age=(datetime.datetime.now()-self.dob)
        self.convert=int(self.age.days)
        self.agesyear=self.convert/356
        if self.agesyear>=18 and self.agesyear<=60:
            print('----------your age is',round(self.agesyear))
        else:
            print('--------enter proper age------------')
        

            

