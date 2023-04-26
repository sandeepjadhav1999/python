#Q: With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary

def dictionary():
    n=int(input('enter the number:'))
    d=dict()
    for i in range(1,n+1):
        d[i]=i**2
    print(d)
dictionary()