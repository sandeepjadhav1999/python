#unpackingmeans it unpacks a given list,tuple,set,to a STRING


def unpacking_seq():
    name=['aa','bb','cc']
    print(name)
    print(*name)

    name=('aa','bb','cc')
    print(name)
    print(*name)

    name={'aa','bb','cc'}
    print(name)
    print(*name)
unpacking_seq()


def sample(start,stop,step):
    for i in range(start,stop,step):
        print(i)
lt=[1,10,2]
sample(*lt)

def sampler(ver,os,stock):
    print(f'version:{ver},os:{os},stock:{stock}')
def unpacking_dict():
    names={'ver':10,'os':'android','stock':11}
    sampler(**names)
    sampler(names.get('ver'),names.get('os'),names.get('stock'))
unpacking_dict()
    
