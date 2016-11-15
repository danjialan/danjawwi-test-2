
def sum(*number):
    sum1 = 0
    for n in number:
        sum1= sum1 + n * n
    return(sum1)

number=[1,2,3,4]
print(sum(*number))
print(sum(*[1,2,3,4]))






