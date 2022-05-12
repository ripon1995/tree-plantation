from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-1q0dc2(u&a7d#8e+nz!wuodgd1kt*48x!bo^(xki!e7%#=11(1'

ALLOWED_HOSTS = ['172.16.226.179', 'desktop-psr46s4.brainstation-23', '10.0.2.2', '192.168.68.108', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TREE',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'rootless'
    }
}
