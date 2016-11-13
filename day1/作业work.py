#!/usr/bin/python
'''
username='danjawwi'
password='123456a'

file=open('login.log','r')
for i in file:

    print(i),

'''
file=open('login.log','r')
un=''
pw=''
j=0



for i in file:
    if j ==0:
        un =i
    if j ==1:
        pw =i
    j = j + 1

print(un)
print(pw)

file=open('lock.log','r')
lock_name=file.readline()

for i in range(3):
    print(lock_name)
    in_uname = input('please enter your name:')
    in_pword = input('please enter your password:')
    if in_uname == lock_name:
        print('no chance')
        file.close()
        break
    elif in_uname in un and in_pword in pw:
        if in_uname == '' or in_pword == '':
            print('please do not enter '' ')
        else:
            print('Welcome')
            break
    else:
        print('your username or password is wrong')

else:
    print('you have used 3 chances,its over')
    file=open('lock.log','a')
    file.write(in_uname)




