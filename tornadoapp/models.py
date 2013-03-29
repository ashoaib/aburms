import re
import datetime

patterns = {
    'name': r"^[A-Za-z\'\-\s]{2,}$",
    'email': r"^[\w\.\+&~-]+@([\w-]+\.{1})+[a-zA-Z]{2,4}$",
    'plain_text': r".{2,}"
}

error_strings = {
    'name': "Please enter a valid name",
    'email': "Please enter a valid email",
    'plain_text': "Please enter valid text"
}

class BaseModel(object):
    def __init__(self):
        self._compiled = {}
        self._errors = {}
        self._timestamp = str(datetime.datetime.now())
        self._collection = str(self.__class__.__name__[:-5]).lower()
        self._compiled['collection'] = self._collection
        
    def set_field(self, field_name, field_type, value):
        if hasattr(self, "_"+field_name):
            if self.validate(field_type, value):
                setattr(self, "_"+field_name, value)
            else:
                setattr(self, "_"+field_name, None)
                self._errors[field_name] = error_strings[field_type]
                
    def validate(self, field_type, value):
        try:
            return re.match(patterns[field_type], value)
        except (re.error, AttributeError):
            return False
        
    def compile(self):
        return self._compiled
    
    @property
    def timestamp(self):
        return self._timestamp
            
    @property
    def collection(self):
        return self._collection
    
    @property
    def errors(self):
        return self._errors
    
    
class ContactModel(BaseModel):
    _name = None
    _email = None
    _message = None
    
    def compile(self):
        self._compiled['document'] = {
            'name': self._name,
            'email': self._email,
            'message': self._message,
            'date_created': self._timestamp
        }
        return self._compiled
    
    @property
    def name(self):
        return self._name['value']
    
    @name.setter
    def name(self, value):
        self.set_field('name', 'name', value)
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self.set_field('email', 'email', value)
        
    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, value):
        self.set_field('message', 'plain_text', value)
        
        
class PostModel(BaseModel):
    _title = None
    _content = None
    
    def compile(self):
        self._compiled['document'] = {
            'title': self._title,
            'content': self._content,
            'date_created': self._timestamp
        }
        return self._compiled
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self.set_field('title', 'plain_text', value)
        
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self.set_field('content', 'plain_text', value)
        
        