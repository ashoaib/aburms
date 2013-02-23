import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.render('error.html')
    
    def site_root(self, sub=''):
        return self.settings['site_root'] + str(sub)
    

class IndexHandler(BaseHandler):
    def get(self):
        data = dict()
        data['meta'] = {
            'title': "Abu Raihan M Shoaib",
            'url': self.site_root(),
            'description': "Personal website of Abu Raihan M Shoaib",
            'site_name': self.settings['site_name']
        }
        data['header_title'] = "me"
        data['body_content'] = "Some text about me"
        data['active'] = "about"
        
        self.render('index.html', **data)


class WorkHandler(BaseHandler):
    def get(self):
        data = dict()
        data['meta'] = {
            'title': "Abu Raihan M Shoaib",
            'url': self.site_root(),
            'description': "Personal website of Abu Raihan M Shoaib",
            'site_name': self.settings['site_name']
        }
        data['header_title'] = "i do"
        data['body_content'] = "Some text about the work i do"
        data['active'] = "work"
        
        self.render('index.html', **data)


class StuffHandler(BaseHandler):
    def get(self):
        data = dict()
        data['meta'] = {
            'title': "Abu Raihan M Shoaib",
            'url': self.site_root(),
            'description': "Personal website of Abu Raihan M Shoaib",
            'site_name': self.settings['site_name']
        }
        data['header_title'] = "i like"
        data['body_content'] = "Some text about stuff i like"
        data['active'] = "stuff"
        
        self.render('index.html', **data)


class ContactHandler(BaseHandler):
    def get(self):
        data = dict()
        data['meta'] = {
            'title': "Abu Raihan M Shoaib",
            'url': self.site_root(),
            'description': "Personal website of Abu Raihan M Shoaib",
            'site_name': self.settings['site_name']
        }
        data['header_title'] = "form"
        data['body_content'] = "the contact form"
        data['active'] = "contact"
        
        self.render('index.html', **data)
        

class ErrorHandler(BaseHandler):
    def get(self):
        raise tornado.web.HTTPError(404)
