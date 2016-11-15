def add_end1(L=[]):
    L.append('END')
    return L
# 为什么会出现这个情况，是因为python 并不管你的L 是在哪里生成的（在之前或者在建立def函数时）
# 所以他只要看到内存里边有了L 的声明定义，就拿来直接用。
# 如果发现L 还没有声明，才会给他声明成默认的 [] .


# 即使你给了参数默认值，即使这个值是有类型的，也没有规定参数的类型。
def add_end2(L=None):
    if L is None:
        L=[]
        L.append('END')
    else:
        L.append('END')
    return L

def add_end3(L=[]):
    if L == []:
        L.append('END')
    else:
        L.append('END')
    return L

print(add_end1())
print(add_end1())
print(add_end1())
print(add_end1(['a','b','c']))
print(add_end1(['a','b','c']))
print(add_end1(['a','b','c']))
print(add_end3())
print(add_end3())
print(add_end3())