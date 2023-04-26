#Q: patter problem

def patterns():
    n=int(input('enter the number of rows:'))
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()
    print('----reverse----')
    for i in range(n):
        for j in range(i,n):
            print('*',end='')
        print()
patterns()