#Q: to convert a given string into uppercase

data=[]
while True:
    inp=input('enter the words with comma:')
    if inp:
        data.append(inp.upper())
    else:
        break
print(*data, sep= ",")