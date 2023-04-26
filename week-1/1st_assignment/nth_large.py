#Q: to find the nth largest element


#im taking the inputs from the user in this code so im using append here to add the elements into the list

def number():
    n=int(input('enter the length of the list:'))
    data=[]
    for i in range(n):
        print('enter the index value of',i)
        lis=int(input())
        data.append(lis)
    print(data)
    num=int(input('enter the nth number:'))
    data.sort()
    print('the',num,'largest number is',data[-num])
number()
