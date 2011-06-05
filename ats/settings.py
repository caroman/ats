# Django settings for ats project.
import os

DEBUG = True 
#DEBUG = False 
TEMPLATE_DEBUG = DEBUG

#SESSION_COOKIE_SECURE = True

ADMINS = (
     ('Carlos Roman', 'caroman@init5.cl'),
)

MANAGERS = ADMINS

#DATABASE_ENGINE = 'postgresql_psycopg2'
#DATABASE_NAME = 'ats'  
#DATABASE_USER = 'ats'
#DATABASE_PASSWORD = 'ats!'
#DATABASE_HOST = ''
#DATABASE_PORT = '5432'  
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'ats',
        'USER': 'ats',
        'PASSWORD': 'ats!',
        'HOST': '',
        'PORT': '5432',
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
SITE_ROOT =  os.path.realpath(os.path.dirname(__file__))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join( SITE_ROOT, 'sitedata/' )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/data/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/ats/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '**g!%rg!is+1r(_u4=k@d!re4f19lhodhds%b9&3ngn*6ify1z'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.transaction.TransactionMiddleware'
)

ROOT_URLCONF = 'ats.urls'

TEMPLATE_DIRS = (
     SITE_ROOT
    ,os.path.join( SITE_ROOT, '/templates' )
    #,'/django/rrhh/trunk/ats'
)

SERIALIZATION_MODULES = {
    'json': 'wadofstuff.django.serializers.json'
    }


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'ats.main',
    'ats.api',
    'ats.static',
)


