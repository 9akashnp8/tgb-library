from decouple import config

ENVIRONMENT = config("ENVIRONMENT")

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .dev import *