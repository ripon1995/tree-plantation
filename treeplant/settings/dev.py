from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-1q0dc2(u&a7d#8e+nz!wuodgd1kt*48x!bo^(xki!e7%#=11(1'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TREE',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'rootless'
    }
}

