from puddle.settings import *
from decouple import config


SECRETE_KEY = config('SECRETE_KEY')
ALLOWED_HOSTS = ['web-production-8000.up.railway.app']