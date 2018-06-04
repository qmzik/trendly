"""
    API-Server for TRENDLY-STYX
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web
import api.handlers.user


def Run(port=8888):
    routes = [
    (r'/api/user/auth', api.handlers.user.UserAuth),
    (r'/api/user/register', api.handlers.user.UserRegister)
    ]

    app = tornado.web.Application(routes)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port)
    print('API-Server on port ', port, ' started')
    tornado.ioloop.IOLoop.instance().start()
