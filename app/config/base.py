"""
    Base Configuration File
"""
""" Put Generic Configurations here """
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'Moo'

""" Put Development Specific Configurations here """
class DevelopmentConfig(Config):
    DEBUG = True

""" Put Staging Specific Configurations here """
class StagingConfig(Config):
    TESTING = True

""" Put Production Specific Configurations here """
class ProductionConfig(Config):
    pass

class ApiKey(object):
   googleMaps = "Moo"
