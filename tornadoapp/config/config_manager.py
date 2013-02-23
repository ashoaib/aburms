import urls, config

class ConfigManager:
    def __init__(self, env=None):
        if env is None:
            raise ValueError('Environment not passed')
        else:
            self._env = env
    
    def get_handlers(self):
        return urls.urls
    
    def get_settings(self):
        if self._env in config.settings:
            env_settings = config.settings[self._env]
            app_settings = config.settings['app']
            return dict(app_settings.items() + env_settings.items())
        else:
            raise KeyError('Environment not set in config')
            