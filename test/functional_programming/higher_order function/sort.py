a = [1,2,3,5,-1,-2,5]
b = sorted(a)
print(b)

c= sorted(a,reverse=True)
print(c)

d = sorted(a,key=abs,reverse=True)
print(d)

a1 = ['a','Z','A','z']

d1 = sorted(a1)
print(d1)
d2= sorted(a1,key=str.lower)
print(d2)