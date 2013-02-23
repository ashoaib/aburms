import tornado.web

class BaseHandler(tornado.web.RequestHandler):
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
