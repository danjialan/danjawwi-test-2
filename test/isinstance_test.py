x=eval(input('please enter int or float:'))
if isinstance(x, (int, float)):
    # print('error input value type')
    # raise TypeError('error input value type')
    print ('error: input bad value type')

def dan_abs(x):
    if eval(x)>=0:
        return (x)
    else :
        return (-eval(x))

print(dan_abs(x))