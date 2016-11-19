def all(w):
    n = 1
    while True:
        if n>=w:
            break
        else:
            n=n+2
            yield n

def all2():
    n = 1
    while True:
        n=n+2
        yield n

def paichu_func(n):
    return lambda x  :  x % n != 0

def sushu(n):
    lis=[]
    p=3
    print(2)
    while p < n:
        lis.append(p)
        p=p+2
    while True:
        a = next (all2)
        if a >= n:
            break
        filter(paichu_func(a),lis)
    print(lis)


