def sampler_runner(start,stop,step):
    if start<5:
        raise Exception(f'ivalid start :{start}')
    if stop>50:
        raise Exception(f'invalid stop:{stop}')
    if step not in [1,2]:
        raise Exception(f'invalid step:{step}')

sampler_runner(6,50,3)