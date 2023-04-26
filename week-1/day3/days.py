def give_me_day():
    days={
        1:'mon',
        2:'tue',
        3:'wed',
        4:'thr',
        5:'fri',
        6:'sat',
        7:'sun'
    }
    return days

def give_me_hoildays():
    return {2,6,8}

print(f'what is my name? {__name__}')

if __name__=='__main__':
    import sys
    print('---this is command line')
    print(sys.argv)
    give_me_day()