def a (x):
    def b (y):
        return x+y
    def c (z):
        return x*z
    if x >2:
        return b
    else:
        return c

p = a(2)(4)
print(p)