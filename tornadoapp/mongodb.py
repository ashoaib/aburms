import ConfigParser
import pymongo

class MongoDB:
    """
    This is a wrapper class for pymongo.
    
    - It reads a .conf file from a path specified in site settings and sets
      config e.g. hostname, port etc.
    - Has methods like get, put to wrap around pymongo functions
    """
    
    def __init__(self, conf_path):
        self._load_config(conf_path)
        
        try:
            self.conn = pymongo.MongoClient(self.config['hostname'], int(self.config['port']))
            self.db = self.conn[self.config['dbname']]
            
            if all(k in self.config for k in ['username', 'password']):
                self._authenticate()
            else:
                print "Warning: mongodb not authenticated on " + str(self.config['dbname'])
        except pymongo.errors.PyMongoError:
            raise Exception('MongoDB connection failed!')
        
    def use(self, db_name):
        self.db = self.conn[db_name]
        
    def get(self, collection, document=dict()):
        try:
            return self.db[collection].find(document)
        except pymongo.errors.PyMongoError:
            return None
    
    def put(self, collection, document=None):
        try:
            return self.db[collection].save(document)
        except pymongo.errors.PyMongoError:
            return None
    
    def update(self, collection, query=dict(), data=None):
        pass
    
    def delete(self, collection, query=dict()):
        pass
    
    def _authenticate(self):
        self.db.authenticate(self.config['username'], self.config['password'])
        
    def _load_config(self, conf_path):
        conf_keys = ['hostname', 'port', 'dbname', 'username', 'password']
        
        try:
            config = ConfigParser.SafeConfigParser()
            config.read(conf_path)
            self.config = {key: config.get('main', key) for key in conf_keys}
        except ConfigParser.NoOptionError:
            raise KeyError('Config options not set correctly')
        except ConfigParser.Error:
            raise IOError('Config file not found at ' + conf_path)
        
            