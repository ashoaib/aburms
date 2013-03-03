from os.path import join, dirname, abspath

root_path = dirname(dirname(abspath(__file__)))
get_folder_path = lambda f: join(root_path, f)

"""
This is the settings dictionary.

- It contains an 'app' key which contains site-specific settings.
- All other keys in settings are environment names, e.g. development, stage, foobar etc.
"""
settings = {
    # Site-specific settings
    'app': {
        'site_name': "abur.ms",
    },

    # Environment settings
    'development': {
        'site_root': 'http://localhost:7186/',
        'port': 7186,
        'static_path': get_folder_path("static"),
        'template_path': get_folder_path("templates"),
        'debug': True,
        'gzip': True,
        'db_conf_path': "/Users/armshoaib/Documents/Programming/Projects/aburms/db.conf"
    },
    
    'stage': {
        'site_root': 'http://stage.abur.ms/',
        'port': 25031,
        'static_path': get_folder_path("static"),
        'template_path': get_folder_path("templates"),
        'debug': False,
        'gzip': True,
        'db_conf_path': "/home/aburms/etc/aburms_stage_db.conf"
    }
}