import base64
import uuid
from os.path import join, dirname, abspath

root_path = dirname(dirname(abspath(__file__)))
get_folder_path = lambda f: join(root_path, f)
secret = lambda s: base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes + s)

"""
This is the settings dictionary.

- It contains an 'app' key which contains site-specific settings.
- All other keys in settings are environment names, e.g. development, stage, foobar etc.
"""
settings = {
    # Site-specific settings
    'app': {
        'site_name': "abur.ms",
        'login_url': "/admin/login"
    },

    # Environment settings
    'development': {
        'site_root': 'http://localhost:7186/',
        'port': 7186,
        'static_path': get_folder_path("static"),
        'template_path': get_folder_path("templates"),
        'debug': True,
        'gzip': True,
        'db_conf_path': "/Users/armshoaib/Documents/Programming/Projects/aburms/db.conf",
        'cookie_secret': secret("development"),
        'xsrf_cookies': True
    },
    
    'stage': {
        'site_root': 'http://stage.abur.ms/',
        'port': 25031,
        'static_path': get_folder_path("static"),
        'template_path': get_folder_path("templates"),
        'debug': False,
        'gzip': True,
        'db_conf_path': "/home/aburms/etc/aburms_stage_db.conf",
        'cookie_secret': secret("stage"),
        'xsrf_cookies': True
    }
}