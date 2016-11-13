dict={
    1: {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3]},
    2: {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3]},
    3: {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3]}
}
for i in dict:
    print (i)

x1=int(input('please enter your 1-st line:'))

for j in dict[x1]:
    print (j)

x2=int(input('please enter your 2-cd line:'))

for k in dict[x1][x2]:
    print (k)

x3=int(input('please enter your 3-rd line:'))

print('%s-%s-%s' %(x1,x2,x3))