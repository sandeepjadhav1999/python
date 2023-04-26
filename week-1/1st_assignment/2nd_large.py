#Q:  2nd largest number

#im taking the inputs from the user in this code so im using append here to add the elements into the list

def numbers():
    n=int(input('enter the length of the list:'))
    data=[]
    for i in range(n):
        print('enter the index value of',i)
        lis=int(input())
        data.append(lis)
    print('the list',data)
    data.sort()
    print('the second largest number is=',data[-2])
numbers()