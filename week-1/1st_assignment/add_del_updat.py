#Q: to add update remove and display from the list

data=[]
print('********add********')
def add(dt):
    data.append(dt)
    print(data)
add(2)
add(3)
add(4)
print('*******remove******')
def remove(dt):
    data.remove(dt)
    print(data)
remove(3)
print('******update*****')
def update(dt):
    data.insert(1,dt)
    print(data)
update(9)
print('****display****')
def display():
    print(data)
display()

    