def all():
    n =1
    while True:
        n=n+2
        yield n

def paichu(k):
   return lambda x:x % k !=0
'''
    def kaohe_guocheng(x):
        if x % k ==0:
            return False
        if x % k !=0:
            return True
'''
def sushu():
    yield 2
    b = all()
    while True:
        a =next(b)
        yield a
        b=filter(paichu(a),b)

for i in sushu():
    if i>= 1000:
        break
    else:
        print(i)


