from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-1q0dc2(u&a7d#8e+nz!wuodgd1kt*48x!bo^(xki!e7%#=11(1'

ALLOWED_HOSTS = ['172.16.226.179', 'desktop-psr46s4.brainstation-23', '10.0.2.2:8080', '192.168.68.108', '127.0.0.1',
                 '172.16.227.86', '172.16.227.255', '172.31.16.1', '0.0.0.0']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tree_data',
        'HOST': 'localhost',
        'USER': "postgres",
        'PASSWORD': 'rootless'
    }
}
