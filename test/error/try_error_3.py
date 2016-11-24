def foo(s):
    c = 10 / s
    return c

def doo(s):
    return  foo(s)*2

def main():
    try:
        doo(0)
    except ZeroDivisionError as we:
        print('error:', we)
    else:
        print('ok')
    finally:
        print('over')

main()