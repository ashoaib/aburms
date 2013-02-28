import ConfigParser
import pymongo

"""
This is a wrapper class for pymongo.

- It reads a .conf file from a path specified in site settings and sets config e.g. hostname, port etc.
- Has methods like get, put to wrap around pymongo functions
"""
class MongoDB:
    def __init__(self, path_to_conf):
        self._load_config(path_to_conf)
        self.conn = pymongo.MongoClient(self._config['hostname'], self._config['port'])
        self.db = self.conn[self._config['dbname']]
        self.db.authenticate(self._config['username'], self._config['password'])
        
    def use(self, db_name):
        self.db = self.conn[db_name]
        
    def get(self, collection, search_dict=dict()):
        return self.db[collection].find(search_dict)
        
    def _load_config(self, path_to_conf):
        conf_keys = ['hostname', 'port', 'username', 'password', 'dbname']
        
        try:
            config = ConfigParser.ConfigParser()
            config.read(path_to_conf)
            self.config = {key: config.get('main', key) for key in conf_keys}
        except ConfigParser.NoOptionError:
            raise KeyError('Config options not set correctly')
        except ConfigParser.Error:
            raise IOError('Config file not found at ' + path_to_conf)
        
#        with open(path_to_conf) as conf_file:
#            self._config = {key: value for (key, value) in conf_file.readlines().split('=')}
#        
#        conf_keys = ['hostname', 'port', 'username', 'password', 'dbname']    
#        
#        for k in conf_keys:
#            if k not in self._config:
#                raise KeyError(k + ' not in config')
        