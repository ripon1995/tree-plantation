from .common import *
import os

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
# SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['treeplantation-backend.herokuapp.com']
