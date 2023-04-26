#Q: strundent marks problem

marks=int(input('enter the marks obtained:'))
if marks>=70:
    print('distinction')
elif marks>60:
    print('pass')
elif marks<=60 and marks>=50:
    print('second class')
elif marks>=40:
    print('thrid class')
elif marks<40:
    print('fail')