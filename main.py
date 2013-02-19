import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from app import handlers, settings

"""
Define global environment - can be anything that's set in the settings dictionary. Suggested values:
    development
    testing
    stage
    production

This is also settable via command line, e.g. -env=production
"""
tornado.options.define("env", default="development", help="Set environment")

"""
Define port for tornado to listen

This can be set here, or in settings, or at the command line, e.g. -port=8888
"""
tornado.options.define("port", default=25031, help="Set port", type=int)

class TornadoApp(tornado.web.Application):
    def __init__(self, env):
        _handlers = handlers.HandlerManager().get_handlers()
        _settings = settings.SettingsManager(env).get_settings()
        tornado.web.Application.__init__(self, _handlers, **_settings)
        

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(TornadoApp(tornado.options.options.env))
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()