import os

print(os.environ)

print(os.path.abspath('.'))

a = [x for x in os.listdir('.')]

print(a)

b = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

print(b)


