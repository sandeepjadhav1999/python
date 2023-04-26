data=[]

def add(dt):
    data.append(dt)
    print(data)
add(12)
add(13)

def remove():
    data.remove(12)
    print(data)
    print('remove')
remove()

def update():
    data.insert(1,1)
    print(data)
    print('update')
update()

def display():
    print(data)
    print('display')
display()
