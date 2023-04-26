def enter_age():
    age=input('enter the age:')
    print(type(age))
    try:
        age=int(age)
    except ValueError:
        age=0
    print(age)
    print(type(age))
enter_age()