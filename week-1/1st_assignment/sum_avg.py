#Q: to find the sum avg max min of numbers

#im taking the inputs from the user in this code so im using append here to add the elements into the list

def basic_math():
    n=int(input('enter the length of the list:'))
    data=[]
    for i in range(n):
        print('enter the index value of ',i)
        lis=int(input())
        data.append(lis)
    print(data)

    print('----sum----')
    print(sum(data))
    print('---avg---')
    print(sum(data)/len(data))
    print('---min---')
    print(min(data))
    print('---max---')
    print(max(data))
basic_math()

