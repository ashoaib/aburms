import tornado.web
import models

from datetime import datetime

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.render('error.html')
    
    def site_root(self, sub=''):
        return self.settings['site_root'] + str(sub)
    
    def render(self, template_name, **kwargs):
        kwargs['site_root'] = self.site_root
        kwargs['year'] = datetime.now().year
        tornado.web.RequestHandler.render(self, template_name, **kwargs)
    

class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')


class WorkHandler(BaseHandler):
    def get(self):
        self.render('work.html')


class StuffHandler(BaseHandler):
    def get(self):
        self.render('stuff.html')


class ContactHandler(BaseHandler):
    def get(self):
        self.render('contact.html', errors=dict())
    
    def post(self):
        contact = models.ContactModel()
        contact.name = self.get_argument('name')
        contact.email = self.get_argument('email')
        contact.message = self.get_argument('message')
        
        if not contact.errors:
            write_id = self.application.db.put(**contact.compile())
            self.render('contact_thanks.html', success=(write_id is not None))
        else:
            self.render('contact.html', errors=contact.errors)
    

class AdminHandler(BaseHandler):
    def get(self):
        self.write('admin')


class ErrorHandler(BaseHandler):
    def get(self):
        raise tornado.web.HTTPError(404)

