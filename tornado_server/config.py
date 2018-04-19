# coding:utf-8
import os
BASE_DIRS= os.path.dirname(__file__)
# 端口参数

options={
    'port':8092,
    'port_list':['koo','pop','lplp']
}
mysql = {
    "host":"localhost",
    "user":'root',
    "pwd":'root',
    'dbName':'tornado_sql',
}
# 配置

settings = {
    # "debug":True,
    # 关闭当前项目的自动转义
    'autoescape':None,
    'autoreload':True,
    # 配置安全cookie密钥
    # import base64
    # >>> import uuid
    # >>> base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)
    'cookie_secret':'KGUzfdrfQ0KpXyMUsD3AfeydgIYUyE4cpMikt2AEsI0=',
    # 开启xsrf保护
    'xsrf_cookies':True,
    'template_path':os.path.join(BASE_DIRS,'templates'),
    'static_path': os.path.join(BASE_DIRS,'static'),
    'login_url':'/verifylogin',
}