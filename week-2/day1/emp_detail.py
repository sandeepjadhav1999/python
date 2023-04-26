class Employee:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def info(self):
        st = str('hos')
        num = int(10)
        arr = list([10, 23, 65])
        st = set([10, 23, 65])
        tpl = tuple([10, 23, 65])
        dct = dict([(1, 'a'), (2, 'b'), ])
        print(st, num)
        print(arr)
        print(st)
        print(tpl)
        print(dct)