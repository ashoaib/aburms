import tornado.web
import models

from datetime import datetime

class BaseHandler(tornado.web.RequestHandler):
    """Base handler containing methods to be used by subclassed handlers"""
    
    def write_error(self, status_code, **kwargs):
        self.render('error.html')
    
    def site_root(self, sub=''):
        return self.settings['site_root'] + str(sub)
    
    def render(self, template_name, **kwargs):
        kwargs['site_root'] = self.site_root
        kwargs['year'] = datetime.now().year
        tornado.web.RequestHandler.render(self, template_name, **kwargs)
    

class IndexHandler(BaseHandler):
    """Handler for /|/about"""
    
    def get(self):
        self.render('index.html')


class WorkHandler(BaseHandler):
    """Handler for /work"""
    
    def get(self):
        self.render('work.html')


class StuffHandler(BaseHandler):
    """Handler for /stuff"""
    
    def get(self):
        self.render('stuff.html')


class ContactHandler(BaseHandler):
    """Handler for /contact"""
    
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
    """Base admin handler for /admin, to be subclassed"""
    
    @tornado.web.authenticated
    def get(self):
        self.render('admin.html')
    
    def get_current_user(self):
        return False
        
        
class AdminLoginHandler(BaseHandler):
    """Admin login handler for /admin/login"""
    
    def get(self):
        self.render('admin.html')
        
    def post(self):
        self.write(self.get_argument('password'))
        
        
class AdminLogoutHandler(BaseHandler):
    """Admin logout handler for /admin/logout"""
    
    def get(self):
        self.write('logout')


class ErrorHandler(BaseHandler):
    """Handler for catching url routes that don't fall into handlers above"""
    
    def get(self):
        raise tornado.web.HTTPError(404)

