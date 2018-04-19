# coding:utf-8
from views.index import HomeLoginHandler,VerifyLoginHandler, PostFile2Handler,CookieNumHandler,SafeCookieHandler,GetCookieHandler,PCookieHandler, MysqlHandler,GetCodeHandler, MarketHandler, EscapeHandler,SoRegHandler, RegisterHandler, UpfileHandler,RenderTestHandler,QrcodeHandler,RequestTestHandler,PostFileHandler,TAO2Handler,TaoHandler, ErrorHandler,IndexHandler,StatusCodeHandler,RedirectHandler,JsonHandler,HeaderHandler
import tornado.web
from views import index
import config,os

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # tornado.web.url(r'/',IndexHandler,{'name':'Miky'},name = 'index'),
            # (r'/',IndexHandler,{'name':'Miky'}),
            (r'/json', JsonHandler),
            (r'/header', HeaderHandler),
            (r'/statuscode',StatusCodeHandler),
            (r'/redirect',RedirectHandler),
            # iserror?flag=2,错误处理
            (r'/error', ErrorHandler),
            tornado.web.url(r'/tao',TaoHandler,{'name':'tao'}),
            (r'/tao2/(\w+)/(\w+)',TAO2Handler),
            (r'/postfile',PostFileHandler),
            (r'/request_test',RequestTestHandler),
            (r'/upfile',UpfileHandler),
            (r'/qrcode',QrcodeHandler),
            (r'/renderTest',RenderTestHandler),
            (r'/register',RegisterHandler),
            (r'/soreg',SoRegHandler),
            (r'/escape',EscapeHandler),
            (r'/market',MarketHandler),
            (r'/getCode', GetCodeHandler),
            (r'/mysql',MysqlHandler),
            (r'/pcookie',PCookieHandler),
            (r'/getcookie',GetCookieHandler),
            (r'/safecookie',SafeCookieHandler),
            (r'/cookienum',CookieNumHandler),
            (r'/postfile2',PostFile2Handler),
            # 登陆验证
            (r'/verifylogin',VerifyLoginHandler),
            (r'/homelogin',HomeLoginHandler),
            (r'/students',index.StudentsHandler),
            (r'/showstudents',index.ShowStudentsHandler),
            (r'/students2',index.Student2Handler),
            (r'/chat',index.ChatHandler),
            (r'/chatpage',index.ChatPageHandler),
            (r'/(.*)$',tornado.web.StaticFileHandler,{"path":os.path.join(config.BASE_DIRS,'static/html'),"default_filename":"index.html"})

        ]
        super(Application,self).__init__(handlers,
                                         **config.settings)
        # self.db=self.application.db
