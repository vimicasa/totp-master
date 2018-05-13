import os

class Config(object):
    APP_NAME = 'Master VCatalan App'
    FOLDER_NAME = 'users'
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'