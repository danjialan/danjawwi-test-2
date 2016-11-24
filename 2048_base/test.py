# letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
#
# print(type(ord))
# print(ord)
#
# print(type(letter_codes))
# print(letter_codes)

# -------***-------***-------***-------***-------***-------***-------***-------***
# list = [1,2,3,4,5,6]
# list2= list *2
# print(list2)
#
# C:\Users\danjawwi\AppData\Local\Programs\Python\Python35-32\python.exe C:/Users/danjawwi/PycharmProjects/danjawwi/2048_base/test.py
# [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# -------***-------***-------***-------***-------***-------***-------***-------***

# tuple1=((1,1),(2,2),(3,3))
# dict1=dict(tuple1)
#
# print(dict1)
# -------***-------***-------***-------***-------***-------***-------***-------***

# field = [[1 for i in range(4)] for j in range(4)]
# print(field)
# -------***-------***-------***-------***-------***-------***-------***-------***

# a = [[1,2,3],[4,5,6],[7,8,9]]
# y = zip(*a)
# print(list(y))
# z= list(map(list,zip(*a)))
# print(z)
# print(list(map(list,zip(*a))))
# print(list(zip(*a)))
# def transpose(field):
#     return [list(r) for r in zip(*field)]
# def invert11(field):
#     return [list(r) for r in field[::-1]]
# print(transpose(a),'def')
# print(invert11(a),'invert11')
# a = [[1,2,3],[4,5,6],[7,8,9]]
# def invert(field):
#     new_field =[]
#     for row in field:
#         new_row = row[::-1]
#         new_field.append(new_row)
#     return new_field
# print(invert(a),'invert')
# a = [1,2,3,4,5,6,7]
# a.append(0)
# print(a)

# a = [1,2,2,4]
# def test1(b):
#     def test(i):
#         if b[i] == 0 and b[i+1] != 0:
#             return True
#         elif b[i] == b[i+1] :
#             return True
#         else:
#             return False
#     return any(test(i) for i in range(len(b)-1))
#
# print(test1(a))
#
# a ='123456'
#
# b= a[1:]
#
# print(b)

# from curses import wrapper
# wrapper(main)
# from collections import defaultdict
#
# def cast(string,):
#     print('\n')
#
#
# def draw_hor_separator():
#     line = '+' + ('+------' * 4 + '+')[1:]
#     separator = defaultdict(lambda: line)
#     if not hasattr(draw_hor_separator, 'counter'):
#         draw_hor_separator.counter = 0
#     cast(separator[draw_hor_separator.counter])
#     draw_hor_separator.counter += 1
#
#
# def draw_row(row):
#     cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')
#
# row = [1000,200,0,4000]
# print(''.join(('|{: ^5}'.format(num) if num > 500 else '| 11' for num in row )) + '|')
# print(''.join('|: ^5'.format(num) if num > 0 else '|     ' for num in row))
# print(''.join(('|{: ^5}'.format(num) if num > 500 else str(num * 2) for num in row )) + '|')

# from curses import wrapper
#
# def main(stdscr):
#     # Clear screen
#     stdscr.clear()
#     stdscr.addstr('111111111111111')
#     # This raises ZeroDivisionError when i == 10.
#     stdscr.refresh()
#     stdscr.getkey()
#
# wrapper(main)
# class Student(object):
#     def __init__(self,name='aaa',age=22):
#         self.name= name
#         self.age = age
#
# dan = Student(age = 5)
# print(dan.name)
# print(dan.age)
#
# width = 4
# height = 4
# field= [[0 for i in range(width)] for j in range(height)]
# print(field)

# a = [[1,2,3],[4,5,6],[7,8,9]]
# b=zip(*a)
#
# print(type(b))
# print(b)
# print(list(b))
#
# print([list(row) for row in zip(*a)])
#
# print((list(list(a) for a in zip(*a))))
# print([list(row[::-1]) for row in a])

def list1(a,b):
    L = []
    for i in range(a):
        for j in range(b):
            L.append((i,j))
    return L

lista = list1(4,4)

print(lista)
