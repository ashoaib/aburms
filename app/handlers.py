import tornado.web
import settings

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        tornado.web.RequestHandler.initialize()
        settings.SettingsManager.get_app_settings()


class IndexHandler(BaseHandler):
    def get(self):
        self.write("index.html")


class WorkHandler(BaseHandler):
    def get(self):
        self.write('work');


class StuffHandler(BaseHandler):
    def get(self):
        self.write('stuff');


class ContactHandler(BaseHandler):
    def get(self):
        self.write('contact');
        
        
class HandlerManager:
    """
    HandlerManager class defines handlers for Tornado
    application and returns the list when called for
    by the app instance
    """
    _handlers = [
        (r"/", IndexHandler),
        (r"/work", WorkHandler),
        (r"/stuff", StuffHandler),
        (r"/contact", ContactHandler)
    ]
    
    def __init__(self):
        # Maybe some code will go here in the future
        pass

    @staticmethod
    def get_handlers(self):
        return self._handlers