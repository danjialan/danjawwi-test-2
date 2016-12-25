def count():
    fs = []
    for i in range(1, 4):
        fs.append(lambda : i * i)
    return fs

print(type(count()))
f = count()
print(type(f))
# print(type(f()))
a,b,c = count()
print(type(a))
print(type(a()))
# print(type(f))
# for i in f:
#     print(type(i))

