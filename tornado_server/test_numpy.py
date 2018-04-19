# coding:utf-8
import numpy

# array1=numpy.array([
#     [12,34,3],
#     [11,66,3],
# ])
# array2=numpy.array([
#     [12,30,10],
#     [11,6,20],
# ])
# k = [val[2] for val in array2]
# print  k
# print array1+array2
# c1=["c1","c2","c3"]
# c2=[12,44,55]
# lp={}
# for k in range(len(c1)):
#     lp[c1[k]]=c2[k]
# print lp
# lp2={key:value for key,value in lp.items()}
# print lp2
# class test():
#     def __init__(self,name):
#         print '%s----%s'%(self,name)
#
# class test2(test):
#     def __init__(self,name):
#         print '%s----%s'%(self,name)
#         super(test2,self).__init__(name)
# c=test2('pppp')
# class Base1(object):
#     def __init__(self):
#         print "我是Base1"
#
#
# class Base2(Base1):
#     def __init__(self):
#         super(Base2, self).__init__()
#         print "我是Base2"
#
#
# class Base(Base2):
#     def __init__(self):
#         super(Base, self).__init__()


# p=Base()

# class ky(object):
#     def __init__(self):
#         print 'kkkkk----%s'%(self)
#
# class ky1(ky):
#     def __init__(self):
#         super(ky1,self).__init__()
#         print 'lp----%s'%(self)
# p=ky1()
#
# class test():
#     @staticmethod
#     def p():
#         print 'this is staticmethod'
#     @classmethod
#     def p2(self):
#         print 'this is classmethod----- ',self
#
#     def p3(self):
#         print self
#
# test().p()
# test.p2()
# test().p3()

# def decor(fn):
#     def f(*args):
#         return '<b>'+fn(*args)+"</b>"
#     return f
#
# @decor
# def p(name):
#     return 'my name is '+name
#
# print p('maty')

# def t(a,b,c):
#
#     print 'a={0},b={1},c={2}'.format(a,b,c)
#
# print t.__class__.__dict__
# p=[12,34,'str']
#
# t(*p)
# p1=(12,2,88)
# t(*p1)
# p2={'a':12,'b':90,'c':77}
# t(*p2)
#
# import socket,time
#
# localhost="62.116.130.8"
# def get_request(path):
#     sock  =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     try:
#         sock.connect((localhost, 8080))
#     except:
#         pass
#     sock.send('GET {} HTTp/1.0\r\n\r\n'.format(path).encode('utf-8'))
#     buffer=[]
#     while True:
#         try:
#             chunk = sock.recv()
#             if chunk:
#                 buffer.append(chunk)
#             else:
#                 break;
#         except:
#             pass
#
#     buffer2 = ''.join(buffer).decode('utf-8')
#     sock.close()
#     print buffer2
#
# get_request('/index')


# class Single_ton(object):
#     __instance=None
#     def __init__(self,name):
#         self.name=name
#     # def __str__(self):
#     #     return 'my Py'
#     def __new__(cls, *args, **kwargs):
#         if (Single_ton.__instance == None):
#             Single_ton.__instance = object.__new__(cls, *args, **kwargs)
#         return Single_ton.__instance
#
# single1=Single_ton("XX")
# single2=Single_ton("YY")
# print single1,single2
# print single1.name,single2.name
#
# class met:
#     name=None
#
# p=met()
# p.name="lplp"
# print p.name
# p2=met()
# print p2.name
import threading
#
# class Single_ton(object):
#     # __instance=None
#     def __new__(cls, *args, **kwargs):
#         # if not hasattr(Single_ton,'__instance'):
# #         if Single_ton.__instance is None:
# #             Single_ton.__instance=object.__new__(cls, *args, **kwargs)
#            if not hasattr(Single_ton, "_instance"):
#
#                Single_ton._instance = Single_ton(*args, **kwargs)
#            return Single_ton._instance
# #
# def task():
#     print id(Single_ton())
#
# def starty():
#     threading.Thread(target=task,args=[]).start()
# for i in range(7):
#     starty()
#
# class Singleton(object):
#
#     def __init__(self):
#         pass
#
#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance
#
# import threading
#
# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()

# lock=threading.Lock()
# class Singal(object):
#     def __init__(self):
#         import time
#         time.sleep(2)
#
#     def __new__(cls, *args, **kwargs):
#         # global lock
#         lock.acquire()
#         if not hasattr(Singal,'_instance'):
#             Singal._instance=object.__new__(cls, *args, **kwargs)
#         lock.release()
#         return Singal._instance
#
# def task(arg):
#     obj = Singal()
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()

# def decor(cls):
#     _instances={}
#     def wrapper(*kw,**kwargs):
#         if cls not in _instances:
#             _instances[cls]=cls(*kw,**kwargs)
#         return _instances[cls]
#     return wrapper
#
# @decor
# class py(object):
#     def __init__(self):
#         pass
#
# def task(arg):
#     obj = py()
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()

# class py(object):
#     # instances=None
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'instance'):
#             cls.instance=object.__new__(cls, *args, **kwargs)
#         return cls.instance

# class p():
#     name=[]
#     def __init__(self):
#         pass
# class d():
#     # pass
#     def __new__(cls, *args, **kwargs):
#         return d(cls, *args, **kwargs)
# class k(d):
#     pass
# print k()
# print d()
# print p()

class Foo(object):
    def __init__(self, *args, **kwargs):
        pass
    def __new__(cls, *args, **kwargs):
        return object.__new__(Stranger, *args, **kwargs)

class Stranger(object):
    pass

foo = Foo()
print foo
print type(foo)
# p.name.append(1112)
# print d.name
# k.name.append(145)
# print p.name
# p.ko=113434534
# print k.ko
# k1=p()
# k1.name.append(12)
# k2=p()
# k2.name.append(111)
# print k1.name

# def task(arg):
#     obj = py()
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()



