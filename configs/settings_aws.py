from .settings_base import *

DEBUG = False

DATABASES['default']['HOST'] = 'db_hostname'
DATABASES['default']['NAME'] = 'db_name'
DATABASES['default']['USER'] = 'user'
DATABASES['default']['PASSWORD'] = 'password'

SERVER_HOST = 'server_hostname'
ALLOWED_HOSTS = [SERVER_HOST]
