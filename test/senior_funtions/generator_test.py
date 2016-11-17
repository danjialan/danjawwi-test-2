
l =[]
a=1
b=1
l.append(a)
l.append(b)
n=2
N=int(input('please input N='))

print(l)

'''
while n<N:
    a = a + b
    print(a,b)
    b = a + b
    print(a,b)
    l.append(a)
    l.append(b)
    print(l)
    n=n+1
'''

while n<N:
    a,b=a+b,a+b*2
    l.append(a)
    l.append(b)
    print(l)
    n=n+1
'''


l =[]
a=1
b=1
l.append(a)
print(l)


'''




