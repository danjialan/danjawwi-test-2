'''
def deco(func):
    c = 1
    def deco1(a,b):
        print('0000')
        ret = func(a,b)
        print('2222',ret+c)
    return deco1

@deco
def prin(a,b):
    print('1111',a,b)
    return a+b

prin(1,2)
prin(5,6)


被装饰的函数最后就变成了同层级的函数了
装饰器在最外边的时候不需要输入参数。
但是这个参数实际上是传入进来了的。
里边调用的时候就需要参数了。
'''

def deco(argu):
    def deco1(fun):
        def deco2(x,y):
            print('000',argu)
            ret = fun(x,y)
            print('222',ret,)
        return deco2
    return deco1

@deco('987')
def prin(a,b):
    print('111',a,b)
    return a+b

prin(1,2)
prin(5,6)


















