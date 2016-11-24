try :
    print('trying.....')
    b= 10
    a= 1.1
    c = b / int('2')
    print(c)
except ValueError as ww:
    print('error:',ww)
except ZeroDivisionError as we:
    print('error:',we)
else:
    print('all is right')
finally:
    print('it is over')
