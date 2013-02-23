import os.path

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
        'port': 25031,
        'static_path': os.path.join(os.path.dirname(__file__), "static"),
        'template_path': os.path.join(os.path.dirname(__file__), "templates"),
        'debug': True,
        'gzip': True
    },
    
    'stage': {
        'port': 25031,
        'static_path': os.path.join(os.path.dirname(__file__), "static"),
        'template_path': os.path.join(os.path.dirname(__file__), "templates"),
        'debug': False,
        'gzip': True
    }
}