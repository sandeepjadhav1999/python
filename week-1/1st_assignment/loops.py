#Q: to find the numbers which are divisible by 7 and not mutliple of 5

str1 = ""
for i in range(2000,3201):
    if (i%7==0) and not (i%5==0):
        str1 = str1+str(i)+","
print(str1.rstrip(","))
