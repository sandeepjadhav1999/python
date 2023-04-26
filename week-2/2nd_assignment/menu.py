def menu():
    print('choose the option:\n1.check the balance\n2.make a create\n3.transfer the amount\n4.deposit money\n5.exit')    
    choice=int(input('enter the choice'))
    return choice
def final():
    while True: 
        state=menu()
        if state==1:
            print('----check the balance---')
        elif state==2:
            print('---create a account---')
        elif state==3:
            print('---transfer the amount----')
        elif state==4:
            print('----deposit amount----')
        elif state==5:
            exit(0)
final()