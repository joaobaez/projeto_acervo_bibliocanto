class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Redudante desde a versão 3.0


class Development(Config):
    DEBUG = True

    SECRET_KEY = 'secret'

    DB_NAME = 'database.db'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'


