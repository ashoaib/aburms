import tornado.web
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
        data = dict()
        data['meta'] = {
            'title': "abur.ms - hello, i'm abu",
            'url': self.site_root(),
            'description': "Personal website of Abu Raihan M Shoaib",
            'site_name': self.settings['site_name']
        }
        data['active'] = "about"
        
        self.render('index.html', **data)


class WorkHandler(BaseHandler):
    def get(self):
        data = dict()
        data['meta'] = {
            'title': "abur.ms - work i do",
            'url': self.site_root("work"),
            'description': "Work done by Abu Raihan M Shoaib",
            'site_name': self.settings['site_name']
        }
        data['active'] = "work"
        
        self.render('work.html', **data)


class StuffHandler(BaseHandler):
    def get(self):
        data = dict()
        data['meta'] = {
            'title': "abur.ms - stuff i like",
            'url': self.site_root("stuff"),
            'description': "Stuff liked by Abu Raihan M Shoaib",
            'site_name': self.settings['site_name']
        }
        data['active'] = "stuff"
        
        self.render('stuff.html', **data)


class ContactHandler(BaseHandler):
    def get(self):
        data = dict()
        data['meta'] = {
            'title': "abur.ms - get in touch",
            'url': self.site_root("contact"),
            'description': "Get in touch with Abu Raihan M Shoaib",
            'site_name': self.settings['site_name']
        }
        data['active'] = "contact"
        
        self.render('contact.html', **data)
        

class ErrorHandler(BaseHandler):
    def get(self):
        raise tornado.web.HTTPError(404)
