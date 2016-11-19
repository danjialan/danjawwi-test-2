'''
a=5

def dan_paichu(n):
    return lambda a:a % n != 0


print(bool(dan_paichu(1)))
print(dan_paichu(2))
'''

def a():
    i =5
    yield i
    yield (i)
    yield 1

a = a()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
