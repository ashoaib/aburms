import tornado.web
import settings

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        tornado.web.RequestHandler.initialize(self)
        settings.SettingsManager.get_app_settings()
    
    def write_error(self, status_code, **kwargs):
        self.write('error occurred')


class IndexHandler(BaseHandler):
    def get(self):
        self.write('about')


class WorkHandler(BaseHandler):
    def get(self):
        self.write('work');


class StuffHandler(BaseHandler):
    def get(self):
        self.write('stuff');


class ContactHandler(BaseHandler):
    def get(self):
        self.write('contact');
        

class ErrorHandler(BaseHandler):
    def get(self):
        self.write('404')
        
    
class HandlerManager:
    """
    HandlerManager class defines handlers for Tornado
    application and returns the list when called for
    by the app instance
    """
    _handlers = [
        (r"/about|/", IndexHandler),
        (r"/work", WorkHandler),
        (r"/stuff", StuffHandler),
        (r"/contact", ContactHandler),
        (r".*", ErrorHandler)
    ]
    
    def __init__(self):
        # Maybe some code will go here in the future
        pass

    def get_handlers(self):
        return self._handlers