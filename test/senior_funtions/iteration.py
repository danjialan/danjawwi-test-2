dan_dict = {'a':1,'b':2,'c':3}
'''
for key in dan_dict:
    print(key)
print('________')
for value in dan_dict.values():
    print(value)
print('________')
for key,value in dan_dict.items():
    print(key,':',value)
print('________')
for key in dan_dict.keys():
    print(key)
'''
from collections import Iterable
print(isinstance('abcdef',Iterable))
print(isinstance(321421,Iterable))
print(isinstance(dan_dict,Iterable))

for i,key in enumerate({'a':'1','b':'2','c':'3'}):
    print(i,key)

for x,y in [(1,4),(2,5),(3,6)]:
    print(x,y)

# iteration 给我感觉就是有点像轮询