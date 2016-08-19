import os


class DevelopConfig:
    TEST = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1:3306/azeroth?charset=utf8'

configs = {
    'default': DevelopConfig,
}

config = configs[os.environ.get('Azeroth', 'default')]