from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'gasto',
       'USER': 'postgres',
       'PASSWORD': 'SANTIjunco11',
       'HOST': 'localhost',
       'PORT': '5432'
   }
}