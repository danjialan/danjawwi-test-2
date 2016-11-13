'''
f=open('test.log','w')
f.write('1\n')
f.write('2\n')
f.write('3\n')
f.write('4\n')
f.close()

'''
f= open ('test.log','r')
j=1
for i in f:
    print (i)
    print ('\n',j)
    j=j+1
f.close()


