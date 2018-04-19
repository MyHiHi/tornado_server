import time

def fib():
    a,b=0,1
    while 1:
        yield  b
        a,b=b,a+b

def caller():
    for i in fib():
        print i

callable()