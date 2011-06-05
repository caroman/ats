from django.conf.urls.defaults import *
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', login, {'template_name':'main/templates/login.html'}),
    (r'^logout/$', logout_then_login, {'login_url':'/ats/'}),
    (r'^api/', include('ats.api.urls')),
    (r'^main/', include('ats.main.urls')),
    (r'^static/', include('ats.static.urls')),
    (r'^admin/', include(admin.site.urls)),
   )
