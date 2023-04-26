#Q: to find the unique elements b/w 2 sets

def unique(set1,set2):
    sets1=set(set1)
    sets2=set(set2)
    print('set1:',sets1)
    print('set2:',sets2)
    print('unique elements are',sets1^sets2)
unique([1,2,3,4,5],[2,4,8,7,8,9])