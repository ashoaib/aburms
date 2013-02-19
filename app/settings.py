import os.path
from tornado.options import options

"""
This is the settings dictionary.

- It contains an 'app' key which contains site-specific settings.
- All other keys in settings are environment names, e.g. development, stage, foobar etc.
"""
settings = {
    # Site-specific settings
    'app': {
        'app_name': "abur.ms"
    },

    # Environment settings
    'development': {
        'port': 12345,
        'static_path': os.path.join(os.path.dirname(__file__), "static"),
        'template_path': os.path.join(os.path.dirname(__file__), "templates"),
        'debug': True
    },
    
    'stage': {
        'port': 25031,
        'static_path': os.path.join(os.path.dirname(__file__), "static"),
        'template_path': os.path.join(os.path.dirname(__file__), "templates"),
        'debug': True
    }
}

class SettingsManager:
    def __init__(self, env):
        """
        - Takes in an argument for the environment.
        - Checks if port is set in environment settings, and 
        supersets any port defined previously.
        - Raises KeyError if environment not found in settings.
        """
        if env in settings:
            self._env = settings[env]
            
            if 'port' in self._env:
                options.port = self._env['port']
        else:
            raise KeyError("Environment not defined in settings")

    def get_settings(self):
        """Returns environment-specific settings dict"""
        return self._env
    
    @staticmethod
    def get_app_settings():
        """Static method for returning site-specific settings dict"""
        return settings['app']