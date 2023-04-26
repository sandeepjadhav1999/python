lst=['hi','bye','hello','fine']
sets={'hi','bye','hello','fine'}
i=set(lst)
print(sets)
print(i)


def sets():
    a={'a','b'}
    b={'b','d'}

    print('--union--')
    print(a.union(b))

    print('--inersectin--')
    print(a.intersection(b))

    print('--difference--')
    print(a.difference(b))

    print('--disjoint--')
    print(a.isdisjoint(b))
sets()