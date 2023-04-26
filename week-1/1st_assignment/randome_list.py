#Q: to remove a random element from a list

#im taking the inputs from the user in this code so im using append here to add the elements into the list

import random
def listed():
    n=int(input('enter the number of elements in the list:-'))
    data=[]
    for i in range(n):
        print('the index value of',i)
        lis=int(input())
        data.append(lis)
    print(f'the list before removing random element {data}')
    print('random element removed for the list',data.pop(random.choice(data)))
    print('the list after randome element being removed',data)
listed()
