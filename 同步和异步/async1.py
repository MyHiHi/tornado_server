# coding:utf-8
# def r():
#     print 'begins'
#     while True:
#         p = yield
#         print 'p= ', p
# kk=None
# def exe(num):
#     global kk
#     kk.send(num)
#
# def rt(num):
#     return '$'+str(num)
# class Bank():
#     risk  = False
#     def create(self):
#         if self.risk ==False:
#             yield  rt(123)
#         else:
#             yield 'None'
# def run():
#     k = Bank().create()
#     return k.next()
# if __name__ =='__main__':
#
#     for i in range(5):
#         print run()
#     Bank.risk = True
#     Bank().risk=False
#     print Bank.risk
#     for i in range(5):
#         print run()

    # global kk
    # kk = r()
    #
    # kk.next()
    # # exe(12)
    # kk.send(234)
    # kk.close()
    # kk.next()

    # my_list = (x*x for x in range(4))
    # print my_list.next(),my_list.next()



#
# def grep(pattern):
#     print "Searching for ",pattern
#     while True:
#         resp = yield
#         if pattern in resp:
#             print resp
#
# c=grep("py")
# c.next()
# c.send('py is a good tool')
# c.send('lp py ui')
# c.send('popopoyyyp')
# c.close()

k  = None
import time
from threading import Thread
def func():
    def run():
        print 'FUNC 开始运行'
        time.sleep(2)
        print 'FUNC 运行结束'
        try:
            global k
            k.send('wwww')
        except StopIteration:
            pass
    Thread(target=run).start()
    return 'finish!'

def decor(func):
    def wrapper():
        global k
        k = func()
        k.next()
    return wrapper

@decor
def requestA():
    print 'requestA 开始运行'
    p = yield func()
    print 'receive :',p
    print 'requestA 结束运行'

def sing_decor(cls):
    def wrapper(*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = cls(*args,**kwargs)
        return cls._instance
    return wrapper
@sing_decor
class Single_ton():
    def __init__(self):
        pass

def main():
    for i in range(13):
        print id(Single_ton())

if __name__=='__main__':

    main()
    # requestA()
    #
    #
    # def r():
    #     list = range(5)
    #     for i in list:
    #         yield i ** 2
    # for k in r():
    #      print k
    # import pickle,io
    # kk = [12,34,45,44,56]
    # byte_dir = io.BytesIO()
    # pickle.dump(kk,byte_dir)
    # print byte_dir.getvalue()
    # byte_dir2 = io.BytesIO()
    # print pickle.loads(byte_dir.getvalue())




