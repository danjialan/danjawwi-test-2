import logging

def doo(s):
    return 10 / s

def coo(s):
    return doo(s) * 2

def main():
    try:
        doo(0)
    except Exception as wr:
        logging.exception(wr)

main()

print('end')


