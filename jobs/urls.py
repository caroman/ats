from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout, logout_then_login

from jobs.main.forms import ProfileForm
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = patterns('',
    # Example:
    (r'^$','jobs.main.views.search'),
    (r'^login/', login,
        {'template_name':'registration/login.html'}),
    (r'^logout/$', logout_then_login,
        {'login_url':'/jobs/login/?next=/jobs/'}) ,
    (r'^accounts/logout/$', logout_then_login,
        {'login_url':'/jobs/login/?next=/jobs/'}) ,
    (r'^accounts/profile/', 'profiles.views.edit_profile',
        {'form_class': ProfileForm,'success_url':'/jobs/profiles/sync/'}),
    (r'^accounts/register/$','registration.views.register', 
        { 'form_class': RegistrationFormUniqueEmail,
          'backend': 'registration.backends.default.DefaultBackend'}),
    (r'^profiles/edit/', 'profiles.views.edit_profile', 
        {'form_class': ProfileForm,'success_url':'/jobs/profiles/sync/'}),
    (r'^profiles/sync/', 'jobs.main.views.profile_sync'),
    #(r'^profiles/edit/', 'profiles.views.edit_profile', {'form_class': ProfileForm}),
    #(r'^profiles/create/', 'profiles.views.create_profile', {'form_class': ProfileForm,}),
    #(r'^profiles/edit/', 'jobs.main.views.edit_profile'),
    #(r'^profiles/create/', 'jobs.main.views.create_profile'),
    #(r'^accounts/profile/', 'jobs.main.views.edit_profile',{'form_class':ProfileForm,'success_url':'/profiles/sync/'}),
    (r'^captcha/', include('captcha.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^job/(?P<job>\d+)/apply/$', 'jobs.main.views.apply'),
    (r'^job/(?P<job>\d+)/detail/$', 'jobs.main.views.detail'),
    (r'^user/applications/', 'jobs.main.views.user_applications'),
    (r'^user/files/', 'jobs.main.views.user_files'),
    (r'^user/file/new/', 'jobs.main.views.userfile_new'),
    (r'^user/file/cv/', 'jobs.main.views.userfile_new', {'resume':True}),
    (r'^data/user/get/(?P<filename>.+)$', 'jobs.main.views.userfile_get'),
    (r'^data/user/del/(?P<filename>.+)$', 'jobs.main.views.userfile_del'),
    (r'^search/$', 'jobs.main.views.search'),
 )
