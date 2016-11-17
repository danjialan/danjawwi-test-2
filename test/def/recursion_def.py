def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(5))

def fact_while(n):
    s =1
    while n>1:
        s = s* n
        n=n-1
    return s

print(fact_while(5))