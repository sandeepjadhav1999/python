def noraml_args(*name):
    print(type(name))
    print(name)
noraml_args('aaa','bbb','ccc')

def kw_args(**names):
    print(type(names))
    print(names)
kw_args(con='aaa',ver='bbb')

def noraml_kw_args(*args,**kwargs):
    print(args)
    print(kwargs)
noraml_kw_args('aa','bb',con='ver',ver='aa')