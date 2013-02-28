import tornado.ioloop
import tornado.options 
import tornado.web
import tornadoapp.mongodb

from tornadoapp.config import config_manager

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
        cm = config_manager.ConfigManager(env)
        _handlers = cm.get_handlers()
        _settings = cm.get_settings()
        
        if 'db_conf_path' in _settings:
            self.set_db(_settings['db_conf_path'])
        else:
            raise KeyError('db_conf_path not found in settings')
        
        if 'port' in _settings:
            tornado.options.options.port = _settings['port']
         
        tornado.web.Application.__init__(self, _handlers, **_settings)
        
    def set_db(self, db_conf_path):
        self.db = tornadoapp.mongodb.MongoDB(db_conf_path)
        

def main():
    tornado.options.parse_command_line()
    tornadoapp_instance = TornadoApp(tornado.options.options.env)
    tornadoapp_instance.listen(tornado.options.options.port)
    print "listening on port:" + str(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()