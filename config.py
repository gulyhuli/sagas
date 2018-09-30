import os


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    API_TOKEN = '646696521:AAEoyHkxFBC8LGtc_nSjh_2AH2lJGuGDcUQ'
    WEB_HOOK_URL = 'https://padavanw31.herokuapp.com'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SECRET_KEY = 'vdadv24t2f'
    BOT_NAME = 'flowsamara_bot'
    IMAGE_DIR = 'files'
    SENDGRID_API_KEY = 'sendgrid api ley'


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'secret'
    BOT_NAME = 'testBot'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    DB_PATH = 'test.db'
    IMAGE_DIR = 'images'


current_config = DevelopmentConfig
