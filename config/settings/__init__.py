# from decouple import config

ENVIRONMENT = 'development'

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .dev import *