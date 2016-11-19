import sys

def hello():
    agrs=sys.argv
    print(type(agrs))
    if len(agrs)==1:
        print('hello 1')
    elif len(agrs)==2:
        print('hello %s %s' %(agrs(0),agrs(1)))
    else:
        print('too many parameters %s' %len(agrs))

if __name__ == '__main__':
    hello()

