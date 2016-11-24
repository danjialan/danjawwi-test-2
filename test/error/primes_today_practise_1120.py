def all():
    n =1
    while True:
        n = n+2
        yield n

def paichu(w):
    return lambda x:x%w !=0

a = paichu(2)(10)
print(type(a))
print(a)

def primes():
    yield 2
    dan_final= all()
    while True:
        w = next(dan_final)
        yield w
        dan_final = filter(paichu(w),dan_final)

weilun_final=[]

for i in primes():
    if i > 100:
        break
    else:
        weilun_final.append(i)

print(weilun_final)