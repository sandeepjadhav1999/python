#Q: to sort the given string


data=input('enter the words:').split(',')
mylist=list(map(str,data))
mylist.sort()
print(*mylist,sep=',')
