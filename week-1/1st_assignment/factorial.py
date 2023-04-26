#Q: to find the factorial

num=int(input('enter the number:'))
res=1
for i in range(num,0,-1):
    res*=i
print(res)