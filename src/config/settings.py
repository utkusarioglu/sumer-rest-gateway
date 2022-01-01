class BaseConfig():
  API_PREFIX = "/rest"
  TESTING = False
  DEBUG = False

class DevelopmentConfig(BaseConfig):
  DEBUG = True

class ProductionConfig(BaseConfig):
  pass

class TestConfig(BaseConfig):
  TESTING = True
  DEBUG = True
