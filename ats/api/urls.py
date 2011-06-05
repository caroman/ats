from django.conf.urls.defaults import *
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login

urlpatterns = patterns('',
    (r'^mandate/list/$', 'ats.api.views.mandate_list'),
    (r'^mandate/list/candidate/(?P<candidate>\d+)/$', 'ats.api.views.mandate_list_candidate'),
    (r'^mandate/(?P<mandate>\d+)/$', 'ats.api.views.mandate_detail'),
    (r'^mandate/(?P<mandate>\d+)/apply/(?P<candidate>\d+)/$', 'ats.api.views.mandate_apply'),
    (r'^candidate/new/$', 'ats.api.views.candidate_new'),
    (r'^candidate/file/new/$', 'ats.api.views.candidatefile_new'),
    (r'^candidate/file/cv/$', 'ats.api.views.candidatefile_new', {'resume':True}),
    (r'^candidate/(?P<candidate>\d+)/update/$', 'ats.api.views.candidate_update'),
    (r'^candidate/(?P<candidate>\d+)/file/list/$', 'ats.api.views.candidatefile_list'),
    (r'^candidate/(?P<candidate>\d+)/file/get/(?P<filename>.+)$', 'ats.api.views.candidatefile_get'),
    (r'^candidate/(?P<candidate>\d+)/file/del/(?P<filename>.+)$', 'ats.api.views.candidatefile_del'),
   )
