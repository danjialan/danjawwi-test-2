def cifang(x,n):
    s= 1
    while n>0:
        s=s*x
        n=n-1
    return (s)

print(cifang(3,3))

#如果只有一个return 的话，就是相当于return None