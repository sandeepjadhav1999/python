"operators"

num1=18
num2=2
def arithmatic():
    print(f'addition is {num1+num2}')
    print(f'subtaction is {num1-num2}')
    print(f'multiplication is {num1*num2}')
    print(f'division is {num1/num2}')
    print(f'exponent is {num1**2}')
    print(f'floor division is {num1//num2}')
    print(f'modulus is {num1%num2}')
arithmatic()

def assignment():
    ver=10
    print(f'the version: {ver}')
    a,b=10,20
    a,b=50,ver
    a+=10
    a-=b
    a*=20
    a=a-b
    a=a*20
    print(f'a,b {a,b}')
assignment()

def bitwise():
    a=10
    b=10
    print(f'and: {a&b}')
    print(f'or: {a|b}')
    print(f'xor: {a^b}')
    print(f'not: {~a}')
    a&=b
    print(f'and: {a}')
bitwise()


def comparision():
    print(f'equal to {num1==num2}')
    print(f'greater than {num1>num2}')
    print(f'lesser than {num1<num2}')
    print(f'greater than equal to {num1>=num2}')
    print(f'lesser than equal to {num1<=num2}')
    print(f'not equal {num1!=num2}')
comparision()


def logical():
    print(f'and :{num1>10 and num2<50}')
    print(f'or :{num1>10 or num2<50}')
    print('or:', not(num1>10 or num2<50))
logical()
