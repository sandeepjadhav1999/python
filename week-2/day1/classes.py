from datetime import date
class abcd:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def print_abc(self):
        print(f'a={self.a},b={self.b},c={self.c}')
class car:
    speed=20 #state
    light=0 #state
    self=10
    #is =10
    #in=10
    def speed_up(self): #behaviour
        self.speed=10
    def turn_on_light(self):  # behaviour
        self.light = 100
    def turn_off_light(self):  # behaviour
        self.light = 0
    def print_car(self):
        print(f' Speed {self.speed}, Light {self.light}')
class age:
    def age_cal(self,dob):
        today=date.today()
        return today.year-dob.year