def all():
    n =1
    while True:
        n= n+2
        yield n
#all() == generator
a = all()
b = all()
print(type(a))

c = bool(a==b)
print(type(c))
print(c)