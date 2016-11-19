# reduce

list1=[1,2,3,4,5,6,7,8,9]

def add(x,y):
    return x+y

def fn(x,y):
    return 10*x+y

from functools import reduce

a = reduce(add,list1)
b = reduce(fn,list1)

print(a)
print(b)



a = '13579'

def char_to_num(s):
    return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}[s]

#f=(map(char_to_num,a))
#print(list(f))
ff=reduce(fn,map(char_to_num,a))
print(ff)










