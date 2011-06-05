from django.contrib import admin
from ats.static.models import *

###############################################################################
class ActivityAdmin( admin.ModelAdmin ):
    list_display = ['priority','title']
    fields = ['priority','title'] 

admin.site.register( Activity, ActivityAdmin )

###############################################################################
class HiringManagerAdmin( admin.ModelAdmin ):
    list_display = ['priority','name']
    fields = ['priority','name'] 

admin.site.register( HiringManager, HiringManagerAdmin )

###############################################################################
class MACStatusAdmin( admin.ModelAdmin ):
    list_display = ['priority','title']
    fields = ['priority','title'] 

admin.site.register( MACStatus, MACStatusAdmin )

###############################################################################
class MandateStatusAdmin( admin.ModelAdmin ):
    list_display = ['priority','title']
    fields = ['priority','title'] 

admin.site.register( MandateStatus, MandateStatusAdmin )

###############################################################################
class ManagmentExperienceAdmin( admin.ModelAdmin ):
    list_display = ['priority','title']
    fields = ['priority','title'] 

admin.site.register( ManagmentExperience, ManagmentExperienceAdmin )

###############################################################################
class ProfessionalDesignationAdmin( admin.ModelAdmin ):
    list_display = ['priority','title']
    fields = ['priority','title'] 

admin.site.register( ProfessionalDesignation, ProfessionalDesignationAdmin )

###############################################################################
class WorkLocationAdmin( admin.ModelAdmin ):
    list_display = ['priority','title']
    fields = ['priority','title'] 

admin.site.register( WorkLocation, WorkLocationAdmin )

###############################################################################
class WorkTypeAdmin( admin.ModelAdmin ):
    list_display = ['priority','title']
    fields = ['priority','title'] 

admin.site.register( WorkType, WorkTypeAdmin )

