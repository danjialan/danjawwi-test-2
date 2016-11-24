def test3():
    n=1
    while True:
        yield n
        n=n+1

a1= next(test3())
a2= next(test3())
a3= next(test3())
a4= next(test3())
a5= next(test3())
print(a1,a2,a3,a4,a5)

tw = test3()
b1= next(tw)
b2= next(tw)
b3= next(tw)
b4= next(tw)
b5= next(tw)
print(b1,b2,b3,b4,b5)
# 我不调用一下的话，他还是知识一个函数，而不是一个generator