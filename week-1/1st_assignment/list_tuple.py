#Q: to convert the given elements into list and tuple

def lists():
    mylist=input('enter the numbers with comma:').split(',')
    mylists=list(map(int,mylist))
    print('list',mylists)
    mytuple=tuple(mylists)
    print('tuple',mytuple)
lists()


# data=[]
# while True:
#     inputs=input('enter the number')
#     if inputs=='':
#         break
#     data.append(int(inputs))
# print('list:',data)
# mytuple=tuple(data)
# print('tuple:',mytuple)