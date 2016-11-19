def count(x,y):
    return lambda: x*x+y

a = count(2,3)
print(a)
print(type(a))

print(a())