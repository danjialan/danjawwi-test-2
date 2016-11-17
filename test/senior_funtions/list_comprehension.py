'''
l1=[x*x for x in range(1,7) if x % 2==0]
print(l1)
l2 =[x * x for x in range(1, 11) if x % 2 == 0]
print(l2)

d = {'a':1,'b':2,'c':3,'d':4}
for k,v in d.items():
    print(k,'=',v)

d = {'a':'1','b':'2','c':'3','d':'4'}
l3 = [ k+'='+v  for k,v in d.items() ]
print (l3)
'''

L = ['Hello', 'World', 18, 'Apple', None]
l=[t.lower() for t in L if isinstance(t,str)]
print(l)

L = ['Hello', 'World',  'Apple']
l=[t.lower() for t in L]
print(l)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])













