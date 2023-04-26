def basics():
    dt='android'
    bt="android 'a' "
    print(dt,bt)
basics()

def multi_line():
    v=10
    dt='''
    this is wither version {ver}
    with the variables will also work
    '''.format(ver=v)
    at=f'''
    this is wither version {v}
    with the variables will also work
    '''
    print(dt)
    print(at)
multi_line()

#TO CHECK IF 2 STRING ARE EQUAL
def str_eqlt():
    nm='android'
    mm='androidm'
    assert nm==mm
    print(f'all is well')
str_eqlt()

#to check the length of the str
def str_length():
    nm='android'
    print(f'the length of the string is {len(nm)}')
str_length()

#to repeat the string
def str_rep():
    print('android\n'*5)
str_rep()