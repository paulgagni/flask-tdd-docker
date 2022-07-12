# src/config.py

#Define environment specific configurations
class BaseConfig:
    TESTING = False

class DevelopmentConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TESTING = True

class ProductionConfig(BaseConfig):
    pass