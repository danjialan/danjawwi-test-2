
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s'%(text,func.__name__))
            return (func(*args,**kw))
        return wrapper
    return decorator

@log('text_test')
def now():
    print('1108')

now()


'''
def tishi(text):
    def shuru_hanshu(func):
        def func_param(a,b):
            print('1:%s  2:%s' %(text,func.__name__))
            return func(a,b)
        return shuru_hanshu
    return tishi

@tishi('1')
def add ():
    print('1')

add(2,3)
'''