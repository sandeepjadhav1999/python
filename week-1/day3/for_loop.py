def basic_loop():
    names=['apple','mango','pineapple','somefruit']
    for i in range(5):
        print(i)
    for name in names:
        print(name,end=',')
basic_loop()

def nested_for():
    for i in range(3):
        print(f'--{i}--')
        for j in range(5):
            print(j,'')
nested_for()

def listeee():
    name=['apple','hi']
    name=[names.upper() for names in name]
    print(name)
listeee()

