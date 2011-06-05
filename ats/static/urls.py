from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^activity/list/$', 'ats.static.views.activity_list'),
    (r'^hiring_manager/list/$', 'ats.static.views.hiring_manager_list'),
    (r'^mac/status/list/$', 'ats.static.views.mac_status_list'),
    (r'^managment_experience/list/$', 'ats.static.views.managment_experience_list'),
    (r'^mandate/status/list/$', 'ats.static.views.mandate_status_list'),
    (r'^professional_designation/list/$', 'ats.static.views.professional_designation_list'),
    (r'^work_location/list/$', 'ats.static.views.work_location_list'),
    (r'^work_type/list/$', 'ats.static.views.work_type_list'),
   )
