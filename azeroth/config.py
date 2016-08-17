import os


class DevelopConfig:
    TEST = True

configs = {
    'default': DevelopConfig,
}

config = configs[os.environ.get('Azeroth', 'default')]