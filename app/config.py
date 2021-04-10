import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Some$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://lab5:postgreslab@localhost/lab5'
    SQLALCHEMY_TRACK_MODIFICATIONS = False #This is just here to suppress a warning from SQLAlchemy as it will soon be removed

    class DevelopmentConfig(Config):
        """Development Config that extends the Base Config Object"""
        DEVELOPMENT = True
        DEBUG = True

    class ProductionConfig(Config):
        """Production Config that extends the Base Config Object"""
        DEBUG = False