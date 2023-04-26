def basics():
    names={
        1: 'abs',
        2: 'poi',
        3: 'tyu'
    }
    print(names)
    print('--',type(names),'--')
    names=dict([(1,'abs'),(2,'poi'),(3,'tyu')])
    print(names)
    print('--',type(names),'--')
    print(type(names.values()))
    print(names.values())
    print(list(names.values()))
    print([*names.values()])
    

    print(type(names.keys()))
    print(names.keys())
    print(set(names.keys()))
    print({*names.keys()})
# basics()

def operation():
    names=dict([(1,'abs'),(2,'zxc'),(3,'asx')])
    names.update({4:'qwe'})
    print(names)
    print(names.get(4))
    print(names.pop(3))
    print(names)
    items_names=list(names.items())
    print(items_names)
    for itm in items_names:
        print(itm)

operation()

