# map

def fang(x):
    return x*x
list1=[1,2,3,4,5,6,7,8,9]
r = map(fang,list1)
print(type(r))
print(list(r))


dan_str= str
r = map(dan_str,list1)
a = list(r)

print(a)