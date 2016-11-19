def a(*arg1):
    def sum():
        j = 0
        for i in arg1:
            j = j + i
        return j
    return sum

d=a (1,2,3,5,4,6,8)

print(d())

f1=a(1,2,3,5,6)
f2=a(1,2,3,5,6)
b= f1==f2
print(type(b))
print(b)
