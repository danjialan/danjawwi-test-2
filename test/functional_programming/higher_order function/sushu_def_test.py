def a():
    x=5
    def b(y):
        z = x+ y
        return (z)

l=[1,2,3,5,6]

p=map(a,l)
print(p)
print(type(p))
print(list(p))