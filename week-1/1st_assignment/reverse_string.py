#Q: to reverse a string using loop

def string(stri):
    for i in range(len(stri)-1,-1,-1):
        print(stri[i],end='')
string('sandeep')