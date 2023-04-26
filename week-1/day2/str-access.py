def access():
    os='android'
    print(f'0th of the string is {os[0]}\n1th element of the string is {os[1]}\n-1th element of the string is {os[-1]}')
access()

def str_slice():
    os='android'
    print('[1:3]',os[1:3])
    print('[-1]',os[-1])
    print('[-3]',os[-3])
    print('[-3:-1]',os[-3:-1])
    print('[:4]',os[:4])
    print('[2:]',os[2:])
    print(os[::-1])
str_slice()