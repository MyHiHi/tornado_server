# coding:utf-8

import time,threading


def longIO():
    def run():
        print '开始耗时操作'
        time.sleep(2)
        print '结束耗时操作'
    threading.Thread(target=run).start()
    yield '这是来自longIO的值'

def async_decor(func):
    def wrapper(*args,**kwargs):
        genA = func(*args,**kwargs)
        gen_longIO = next(genA)
        def run(ey):
            try:
                res = next(ey)
                genA.send(res)
            except StopIteration:
                pass
        threading.Thread(target=run,args=(gen_longIO,)).start()
    return wrapper

@async_decor
def reqA():
    print '开始执行A'
    p = yield longIO()
    print ' p = ',p
    print '结束执行A'

reqA()

def r():
    print 'rrrr1'
    yield 'response'
    print 'rrrrr2'
print '***',r()
print r().next()