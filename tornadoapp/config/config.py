from os.path import join, dirname, abspath

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
        'port': 7186,
        'static_path': join(dirname(dirname(abspath(__file__))), "static"),
        'template_path': join(dirname(dirname(abspath(__file__))), "templates"),
        'debug': True,
        'gzip': True
    },
    
    'stage': {
        'port': 25031,
        'static_path': join(dirname(dirname(abspath(__file__))), "static"),
        'template_path': join(dirname(dirname(abspath(__file__))), "templates"),
        'debug': False,
        'gzip': True
    }
}