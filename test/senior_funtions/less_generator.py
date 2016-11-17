'''
def lib(max):
    n=2
    a=1
    b=1
    print(a,b)
    while n <max:
        a,b=b,a+b
        print(b)
        n=n+1

lib(5)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield
    print('step 3')
    yield (3)

o=odd()

next (o)
next (o)
next (o)
#这里有一个可笑的事情是，我的odd在不附加给一个参数的时候 好像在内存里边还不会被存储。
'''

def lib(max):
    n=2
    a=1
    b=1
    print(a,b)
    while n <max:
        a,b=b,a+b
        yield(b)
        n=n+1
    return 'done'

for n in lib(5):
    print(n)
