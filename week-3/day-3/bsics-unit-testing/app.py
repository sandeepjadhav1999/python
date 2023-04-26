'''
num shd be greater than 10
result she be greater 10
num1 shd be less than num2
negative numbers are not allowed
zeros are not allowed
'''

def add(num1:int,num2:int):
    if num1>10 and num2>10 and num1<num2:
        res=num1+num2
        if res<10:
            return -3
        else:
            return res        
    return -1
