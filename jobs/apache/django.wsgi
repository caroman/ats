import os
import sys

thisrealpath = os.path.realpath( __file__ )
apache_configuration = os.path.dirname( thisrealpath )
project = os.path.dirname( apache_configuration )
workspace = os.path.dirname(project)

if workspace not in sys.path:
    sys.path.append( workspace ) 

os.environ['DJANGO_SETTINGS_MODULE'] = 'jobs.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


