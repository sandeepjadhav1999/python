#Q: capitalize the nth element

def capit(n,str_dt):
    print(str_dt[:n].lower()+str_dt[n:].capitalize())
capit(1,'abcd')