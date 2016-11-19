'''
def strip(s):
    return s

a=['a','','b','','c']
print(a)
k=filter(strip,a)
print(k)
print(list(k))

s =''
print('-',s.strip(),'-')
'''
def dan_all():
    n= 1
    while True:
        n = n + 2
        yield n


def dan_paichu(n):
    return lambda x: x % n > 0

def dan_sushu():
    yield 2
    danin = dan_all()
    while True:
        n = next(danin)
        yield n
        danin = filter(dan_paichu(n),danin)


for i in dan_sushu():
    if i > 1000:
        break
    else:
        print(i)




