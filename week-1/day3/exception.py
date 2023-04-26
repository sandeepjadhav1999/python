def calculate(num1,num2):
    return num1/num2

# print(f'the result is {calculate(10,20)}')
# print(f'the result is {calculate(50,98)}')
# print(f'the result is {calculate(1,1)}')
# print(f'the result is {calculate(0,1)}')
# print('this is python')

# def list_prop(n):
#     numes=[10,20,30]
#     print(numes[n])
# list_prop(1)
# list_prop(10)

def cal(num1,num2,n):
    names=[10,20,30]
    try:
        res=num1/num2 + names[n]
    except ZeroDivisionError:
        res=0
    except IndexError:
        res=-1
    return res

print(f'the result is {cal(10,20,1)}')
print(f'the result is {cal(50,98,0)}')
print(f'the result is {cal(1,1,0)}')
print(f'the result is {cal(0,1,10)}')