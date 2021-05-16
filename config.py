class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///titanic.sqlite3"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://issrrbbbwqlmbl:9198288aea2523075436169ea74e9914b81697891fb3075ce1915a7e7d405013@ec2-35-174-118-71.compute-1.amazonaws.com:5432/d758eese0nfeeu"
