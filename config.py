# -*- coding: utf-8 -*-
class Config(object):
        
    APP_NAME = 'GenericBackend'
        
class ProductionConfig(Config):
    
    ENV = 'production'
    DEBUG = False
    PORT = 5005
    BACKEND_PORT = 5000
    BACKEND_URI = 'localhost'
    #SQLALCHEMY_ECHO = False
    #DATABASE_PATH = 'sqlite:///%s/db/%s.db' % (_os.path.abspath(_os.getcwd()), 'prod')

    
class DevConfig(Config):

    ENV = 'development'
    DEBUG = True        
    PORT = 5003
    BACKEND_PORT = 5000
    BACKEND_URI = 'localhost'
    #SQLALCHEMY_ECHO = True 
    #DATABASE_PATH = 'sqlite:///%s/db/%s.db' % (_os.path.abspath(_os.getcwd()), 'dev')
    
    
app_config = {'PROD': ProductionConfig,
              'DEV' : DevConfig}