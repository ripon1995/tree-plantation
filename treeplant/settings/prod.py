from .common import *
import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
# SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['treeplantation-backend.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}
