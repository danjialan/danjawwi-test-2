try:
    a =10
    b= 2
    c = a / b
    print(c)
except ZeroDivisionError as w:
    print('error:',w)
finally:
    print('its finished')
