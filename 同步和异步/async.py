# coding=utf-8
import time,threading

# def thread_run(fn):
#     def run(*args):
#         print args,'start'
#         fn(*args)
#         print args,'over'
#     return threading.Thread(target=run).start()
# @thread_run
# def fn1(name):
#     print name,'begin......'
# @thread_run
# def fn2(name):
#     print name,'begin'
#
# if __name__=='__main__':
#     print '开始程序'
#     time.sleep(5)
#     fn1('方法1')
#     time.sleep(5)
#     fn2('方法2')
#     print '结束程序'
#
def cc(fn):
    th = threading.Thread(target=fn)
    th.start()
    th.join()
# def f():
#     def run():
#         print 'begin.f...'
#         time.sleep(5)
#         print 'over.f...'
#     cc(run)
#
# def f1():
#     def run():
#         print 'begin..f1..'
#         time.sleep(5)
#         print 'over...f1.'
#     cc(run)
# if __name__=='__main__':
#     print 'start....'
#     time.sleep(5)
#     f()
#     f1()
#     # threading.Thread.daemon=True
#     print 'end...'

#
# def fn2(callback):
#     def run(cb):
#         print '开始处理耗时操作fn2'
#         time.sleep(3)
#         print '处理耗时操作fn2结束'
#         cb('这是fn2 的返回值')
#     th=threading.Thread(target=run,args=(callback,))
#     th.start()
#     th.join()
#     # cc(run)
#
# def finish(res):
#     print '开始处理回调函数'
#     print '接收到fn2的数据:',res
#     print '结束处理回调函数'
#
# def fn3():
#     def run():
#         print '开始处理fn3'
#         time.sleep(1)
#         fn2(finish)
#         # print '从fn2接收到 ',res
#         print '处理fn3结束'
#     cc(run)
# def fn4():
#     print '开始处理fn4'
#     time.sleep(1)
#     print '处理fn4结束'
# if __name__=="__main__":
#     print '开始主线程'
#     # fn2()
#     time.sleep(1)
#     fn3()
#     fn4()
#     print '结束主线程'
#
# gen=None
# def base():
#     def run():
#         print '开始耗时操作'
#         time.sleep(2)
#         try:
#             global gen;
#             gen.send("返回值")
#         except:
#             print '****error****'
#         print '结束耗时操作'
#     cc(run)
# def genCo(func):
#     def wrapper(*args,**kwargs):
#         global  gen
#         gen=func(*args,**kwargs)
#         next(gen)
#     return wrapper
#
# @genCo
# def reqA():
#     print '开始处理reqA'
#     res=yield base()
#     print '接受到来自base的值: ',res
#     print '结束处理reqA'
#
# def reqB():
#     print '开始处理reqB'
#     time.sleep(1)
#     print '结束处理reqB'
#
#
# def main():
#     # global gen
#     # gen = reqA()
#     # next(gen)
#     reqA()
#     reqB()
#     while 1:
#         pass
# if __name__=='__main__':
#     main()
#
# def run():
#     print '开始耗时操作'
#     time.sleep(2)
#     print '结束耗时操作'
#     yield  'yeartty'
#
# def genCo(func):
#     def wrapper(*args,**kwargs):
#         gen1=func(*args,**kwargs)
#         gen2=next(gen1)
#         def run(g):
#             res=next(g)
#             try:
#                 gen1.send(res)
#             except:
#                 pass
#         threading.Thread(target=run,args=(gen2,)).start()
#     return wrapper
#  def fib():
#      a, b = 0, 1
#      while 1:
#         yield b
#         a, b = b, a+b
#
#
# def caller():
#     for i in next(fib()):
#         print i
#
# callable()

# import tornado.ioloop
# from tornado.gen import coroutine
# from tornado.concurrent import Future
#
# @coroutine
# def asyn_sum(a, b):
#     print("begin calculate:sum %d+%d"%(a,b))
#     future = Future()
#
#     def callback(a, b):
#         print("calculating the sum of %d+%d:"%(a,b))
#         future.set_result(a+b)
#     tornado.ioloop.IOLoop.instance().add_callback(callback, a, b)
#
#     result = yield future
#
#     print("after yielded")
#     print("the %d+%d=%d"%(a, b, result))
#
# def main():
#     asyn_sum(2,3)
#     tornado.ioloop.IOLoop.instance().start()
#
# if __name__ == "__main__":
#     main()

gen=None
# def longIO(func):
def longIO():
    def run():
    # def run(cb):
        print "开始处理longIO"
        time.sleep(3)
        try:
            global gen
            gen.send("sunck maker")
        except StopIteration as e:
            pass
        # print "结束处理longIO"
        # cb(" sunck makes ")
    # th = threading.Thread(target=run,args=(func,))
    # th.start()
    th = threading.Thread(target=run)
    th.start()
    # th.join()

# def finish(data):
#     print "开始处理回调函数"
#     print "接受到的数据 :",data
#     print "结束处理回调函数"

def decor(func):
    def wrapper(*args,**kwargs):
        global gen
        gen = func(*args,**kwargs)
        # next(gen)
        gen.next()
    return wrapper

@decor
def request():
    print "开始处理request"
    res = yield longIO()
    print "接受到的数据 :", res
    print "结束处理request"

def requestB():
    print "开始处理requestB"
    time.sleep(2)
    print "结束处理requestB"

def main():
    request()
    requestB()


def cc(run):
    th = threading.Thread(target=run)
    th.start()
    th.join()

kk=None
def exe(num):
    global kk
    kk.send(222)
def main2():
    # print "lll"
    p = yield exe(89)
    print 'p = ',p
if __name__=='__main__':
    start=time.time()
    global kk
    kk=main2()
    kk.next()
    # main()
    print "结束时间：%.2f"%(time.time()-start)
