
# coding:utf-8
from tornado.web import RequestHandler
import json
import config,os
class IndexHandler(RequestHandler):
    def initialize(self,name):
        self.name = name
    def get(self, *args, **kwargs):
        self.write('hello Py')

class JsonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            'name':'Miky',
            'age':21,
            'hobby':'swim'
        }
        # json_str = json.dumps(per)
        # self.write(json_str)
        self.set_header('Content-Type','Application/json;Charset=utf-8')
        self.write(per)

class HeaderHandler(RequestHandler):
    # 先于http请求执行
    def set_default_headers(self):
        self.set_header('Content-Type','text/html;charset=UTF-8')
    def get(self, *args, **kwargs):
        self.set_header('taotao','handsome')
        self.write('header')
    def post(self, *args, **kwargs):
        pass


class StatusCodeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(404,'no foooound')
        self.write('ddddd')


class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # url= self.reverse_url('taoo')

        self.redirect('/')

class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code==500:
            # self.set_status()
            self.write('Internal Server Error!!!!!!')
        elif status_code==404:
            self.write('资源不存在')
        else:
            self.write('未知错误')

        self.set_status(status_code,'EERROORR')

    def get(self, *args, **kwargs):
        flag=self.get_query_argument('flag')
        if flag=='0':
            self.send_error(status_code=500)
        else:
            # self.write('correct response')
            self.redirect('/header')



class TaoHandler(RequestHandler):
    def initialize(self,name):
        self.name=name
    def get(self, *args, **kwargs):
        # print self.name,'*(*(*(*)*)*)'
        self.write(self.name)
        self.write('******')
        # 获取到路由为’index‘的正则匹配

        url = self.reverse_url(name='index')
        self.write('<a href="{0}">去HEADER</a>'.format(url))


class TAO2Handler (RequestHandler):
    def get(self, h1,h2,*args, **kwargs):
        print 'h1 = ',h1,'h2 = ',h2
        self.write('pyTHon>')

class PostFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name')
        # name = self.get_argument('name')
        pwd = self.get_body_argument('pwd')
        hobby = self.get_body_arguments('hobby')
        plan = self.get_body_argument('plan')

        self.write(name+'****'+pwd+'*****'+str(hobby)+'******'+plan)

class RequestTestHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print self.request

        self.write(str(self.request.uri))

class UpfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):



        files= self.request.files
        for file in files:

            for k in files.get(file):
                file_path = os.path.join(config.BASE_DIRS,'upfiles\\'+k.filename)
                with open(file_path,'wb') as f:
                    f.write(k.body);
                # filename = k.get('filename')
                # with open(r'e:\%s'%(filename),'wb') as f:
                #     f.write(k.get('body'))
        self.write(os.path.dirname(__file__))
        self.write('ok')
                # print k.get('body')
        # self.write(str(files))
        # with open('e:\\p.png','wb') as f:
        #     f.write(files[0].get('body'))
            # for file in files[0].get('body').chunks():
            #     f.write(file);
import qrcode
import os
import config,io
# from django.utils.six import BytesIO
from io import BytesIO

class GetCodeHandler(RequestHandler):
    def get(self):
        self.render('getCode.html',title = '获取二维码')
class QrcodeHandler(RequestHandler):
    # def set_default_headers(self):
    #     self.write('set_default_headers\n')
    # def initialize(self):
    #     self.write('initialize\n')
    # def prepare(self):
    #     self.write('prepare\n')
    # def get(self, *args, **kwargs):
    #     self.write('get\n')
    # def write_error(self, status_code, **kwargs):
    #     self.write('write_error\n')
    # def on_finish(self):
    #
    #     self.write('on_finish\n')
    def post(self):
        # info = 'i am zhangtao'
        # img = qrcode.make(info)
        # path = os.path.join(config.BASE_DIRS, 'static\\images\\test.png')
        # with open(path,'wb') as f:
        #     img.save(f)
        # self.set_header('Content-Type','image/png')
        # # dir2= BytesIO()
        # # img.save(dir2)
        # # self.write(dir2.getvalue())
        # with open(path,'rb') as f:
        #     self.write(f.read())
        # self.write('ok')
        # info = str(input("输入信息"))
        info = str(self.get_body_argument('qrcode'))
        code = qrcode.make(info)
        space  = BytesIO()
        self.set_header('Content-Type','image/png')
        code.save(space)
        self.write(space.getvalue())


class RenderTestHandler(RequestHandler):
    def get(self, *args, **kwargs):
        per={
            'name':'tao',
            'age':21,
        }
        stu=[
            {'name':'Miky','age':13},
            {'name':'Pouy','age':14},
        ]
        def getSum(a,b):
            return a+b
        # print os.path.dirname(__file__)
        self.render('home.html',getSum=getSum,num=100,per=per,stu=stu)

class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html')
class SoRegHandler(RequestHandler):
    def post(self):
        name  = self.get_body_argument('name')
        if  name:
            # self.write("alert('恭喜 {0} 注册成功!')".format(name))
            info = 'i am '+name
            img = qrcode.make(info.decode('gbk'))
            dir= BytesIO()
            img.save(dir)
            self.set_header('Content-Type','html/png')
            self.write(dir.getvalue())
        if not name:
            self.write(' raw alert("请输入姓名")')

class EscapeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        test_str = '<h1>hello python</h1>'
        self.render('escapeTest.html',tip1 = '这是转义的结果',str= test_str,tip2 = '这是raw 取消转义的结果',str2= test_str)
class MarketHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('market.html',title='市场')
from models import Students
class MysqlHandler(RequestHandler):
    def get(self, *args, **kwargs):
        name="ss"
        age=13
        stu=Students(name,age)
        stu.delete()
        # stu.save()
        # findOne = stu.find_one(name,age)
        # if findOne==None:
        #     print "没有"
        # else:
        #     for i in stu.find_one(name,age):
        #         print i
        # info=stu.find_all()
        # for i in info:
        #     print i
        self.write('ok')
class PCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        flag = self.get_query_argument('cook')
        if flag=='0':
            self.set_cookie('name', 'tao')
        elif flag=='1':
            self.clear_cookie('name')

        name = self.get_cookie('name', '未登录')
        self.write(name)
        print type(flag)
        # self.write('ok')

class GetCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        cookie_name=self.get_cookie('pwd',default='未登录')
        self.write(cookie_name)
class SafeCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 设置一个带有签名和时间戳
        flag=self.get_query_argument('f')
        if flag=='1':
            self.set_secure_cookie('age', '14')
            self.write('ok')

        else:
            self.write(self.get_secure_cookie('age'))

class CookieNumHandler(RequestHandler):
    def prepare(self):
        cookie_num = int(self.get_cookie('cou', 0))
        if cookie_num>10:
            self.send_error(500)
    def write_error(self, status_code, **kwargs):
        if status_code==500:
            self.write('你访问的次数过多!')
    def get(self, *args, **kwargs):
        cookie_num = int(self.get_cookie('cou', 0))
        self.write('你是第{0}次访问'.format(cookie_num))
class PostFile2Handler(RequestHandler):
    def get(self):
        self.render('login.html')
    def post(self, *args, **kwargs):
        cookie_num = int(self.get_cookie('cou', 0))
        name = self.get_body_argument('name')
        print name+"******"
        if not cookie_num:
            cookie_num = 1
        else:
            cookie_num += 1
        self.set_cookie('cou', str(cookie_num))
        # self.redirect('/cookienum')

import tornado
class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(StaticFileHandler,self).__init__(*args,**kwargs)
        self.xsrf_token

# 用户验证
class VerifyLoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # next = self.get_argument('next', '/')
        # url="/verifylogin?next="+next
        self.render('login.html')
    def post(self, *args, **kwargs):
        name = self.get_body_argument('name')
        pwd = self.get_body_argument('pwd')
        if name=='1' and pwd=='1':
            next = self.get_argument('next', '/')
            self.redirect(next+'?flag=logined')
        else:
            next = self.get_argument('next', '/')
            self.redirect("/"+next)



class HomeLoginHandler(RequestHandler):
    def get_current_user(self):
        flag=self.get_argument('flag',None)
        return flag
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('homes.html')
import time,json,urllib2
from tornado.httpclient import AsyncHTTPClient

# 回调函数实现网络访问
class StudentsHandler(RequestHandler):
    def on_response(self,response):
        print '***'
        if response.error:

            self.send_error(404)
        else:
            data = json.loads(response.body)
            self.write(data)
        self.finish()
     # 不关闭通信的通道
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        # time.sleep(5)
        url='http://www.baidu.com'
        # 创建客户端
        client = AsyncHTTPClient()
        client.fetch(url,self.on_response)
        # data = urllib2.urlopen(url)

        # self.write(data)

# 协程实现网络访问
class ShowStudentsHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = 'http://www.baidu.com'
        # 创建客户端
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res.body)
            self.write(data)
# 协程实现网络访问 网络访问分离
class Student2Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        res = yield self.getData()
        self.write(res)


    def getData(self):
        url = 'http://www.baidu.com'
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            rep = {"rep":'0'}
        else:
            rep =json.loads(res.body)
        raise tornado.gen.Return(rep)

class ChatPageHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('chat.html')
from tornado.websocket import WebSocketHandler
class ChatHandler(WebSocketHandler):
    users=[]
    # 当一个webSocket连接建立时被调用
    def open(self, *args, **kwargs):
        self.users.append(self)
        for user in self.users:
            # message可以是string或dict(json)
            # binary:False(utf-8) True(二进制) default:False
            user.write_message(u"[%s]登陆了"%(self.request.remote_ip),binary=False)

    # 当webSocket 客户端关闭连接后调用
    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            # message可以是string或dict(json)
            # binary:False(utf-8) True(二进制) default:False
            user.write_message(u"[%s]下线了" % (self.request.remote_ip), binary=False)

    # 当客户端发送消息过来时调用
    def on_message(self, message):
        for user in self.users:
            # message可以是string或dict(json)
            # binary:False(utf-8) True(二进制) default:False
            user.write_message(u"[%s] 说:%s" % (self.request.remote_ip,message), binary=False,)

    # 对符合条件的请求源允许连接，同源策略
    def check_origin(self, origin):
        return True
    # 服务器关闭连接
    def close(self, code=None, reason=None):
        pass

