#Q: Formula problem

import math
number=input('enter the number with comma:').split(',')
data=[]
for i in number:
    q=round(math.sqrt(2*50*int(i)/30))
    data.append(q)
print(*data,sep=',')