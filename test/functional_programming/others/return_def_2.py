'''
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

dt=count()
print(dt)
print(type(dt))
#print(dt())
a,b,c=dt
# 如果是一个list的话，可以用a,b,c,d=list 来代替list中的每一个值。
print(a)
print(type(a))

print(a())
'''

def count():
    fs = []
    def a(i):
        def b():
            return i*i
        return b
    for q in range(1,4):
        fs.append(a(q))
    return fs

a,b,c=count()
print(a())
print(b())
print(c())

