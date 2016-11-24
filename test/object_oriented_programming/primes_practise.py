def all():
    n= 1
    while True:
        n=n+2
        yield n

def paichu(n):
    return lambda x : x % n != 0

def primes():
    yield 2
    s= all()
    while True:
        a = next(s)
        yield a
        s=filter(paichu(a),s)

for i in primes():
    if i < 100:
        print(i)
    else:
        break
