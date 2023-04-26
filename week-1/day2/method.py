"methods/functions and its definition"
#normal function call 1
def info():
    print('hi')

#normasl function call 2
def info_detail():
    print('hello')

#function with passing the agruments
def info_with_parameter(sand,eep):
    print(f'is SQL= {sand}')
    print(f'connection= {eep}')

#function with a return statement
def info_with_return():
    print('im returing the value')
    return 20

#function with changing the agrument places
def info_parameter(sql=True,con='deafult'):
    print(f'is sql={sql}')
    print(f'is connection={con}')


    

info()
info_detail()
info_with_parameter(True,'www.abc.com')
ret=info_with_return()
print(f'return value is ={ret}')

info_parameter(False,'www.abc.com')
info_parameter(con='www.sandeep.com',sql=False)
info_parameter()


