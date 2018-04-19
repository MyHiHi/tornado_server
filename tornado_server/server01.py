
import tornado.ioloop,tornado.options

import config
import application
if __name__=='__main__':
    # tornado.op  tions.options.logging  = None

    app = application.Application()
    app.listen(config.options.get('port'))
    tornado.ioloop.IOLoop.current().start()