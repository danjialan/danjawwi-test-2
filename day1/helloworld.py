'''
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}

for k in dict:
    print ("dict[%s] =" %k,dict[k])

for k in dict:
    print ("dict[$k] =",dict[k])

dict = {"a" : ("apple",), "bo" : {"b" : "banana", "o" : "orange"}, "g" : ["grape","grapefruit"]}
print(dict['a'])
print(dict['a'][0])
print(dict['bo']['b'])
print(dict['g'][1])
'''

dict = {1 : ("apple",), 2 : {"b" : "banana", "o" : "orange"}, 3 : ["grape","grapefruit"]}
x=1
print(dict[x])
print(dict['a'][0])
print(dict['bo']['b'])
print(dict['g'][1])