# src/config.py

#define environment-specific configuration variables
class BaseConfig:
    TESTING = False

class DevelopmentConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TESTING = True

class ProductionConfig(BaseConfig):
    pass
