def dt_fn():
    print('this is abc')

def pt_fn(gtn):
    gtn()

fn=dt_fn
pt_fn(fn)
pt_fn(dt_fn)


def rt_fn():
    ds=dt_fn
    return ds

fd=rt_fn()
fd()
