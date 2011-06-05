from django.contrib import admin
from ats.main.models import *

###############################################################################
class CandidateAdmin( admin.ModelAdmin ):
    #List
    list_display = [
         'id'
        ,'first_name'
        ,'last_name'
        ,'phone'
        ,'email_1'
        ,'created_by'
        ,'created_time'
        ,'updated_by'
        ,'updated_time'
        ]
    #list_display_links = ('name',)
    list_filter = [
        'created_by'
        ]
    search_fields = [
         'id'
        ,'first_name'
        ,'last_name'
        ,'phone'
        ,'mobile'
        ,'email_1'
        ,'email_2'
        ,'address'
        ,'city'
        ,'statte'
        ,'postal_code'
        ,'created_by__username'
        ,'created_time'
        ,'updated_by__username'
        ,'updated_time'
         ]
    list_select_related = True
    fields = [
         'first_name'
        ,'last_name'
        ,'phone'
        ,'mobile'
        ,'email_1'
        ,'email_2'
        ,'address'
        ,'city'
        ,'state'
        ,'postal_code'
        ,'professional_designations'
        ,'managment_experience'
        ,'work_locations'
        ,'salary'
        ,'work_types'
        ,'keywords'
        ]

    def save_model( self, request, obj, form, change ):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
            obj.updated_by = request.user
        obj.save()
    
admin.site.register( Candidate, CandidateAdmin )

###############################################################################
class CandidateFileAdmin( admin.ModelAdmin ):
    list_display = [
         'title'
        ,'candidate'
        ,'created_by'
        ,'created_time'
        ]
    fields = [
         'title'
        ,'candidate'
        ,'file'
        ] 

    def save_model( self, request, obj, form, change ):
        obj.created_by = request.user
        obj.save()
 
admin.site.register( CandidateFile, CandidateFileAdmin )


###############################################################################
class MandateAdmin( admin.ModelAdmin ):
    list_display = [
         'id'
        ,'title'
        ,'status'
        ,'created_by'
        ,'posting_start_date'
        ,'posting_end_date'
        ]
    search_fields = [
         'id'
        ,'title'
        ,'status__title'
        ,'created_by__username'
        ,'posting_start_date'
        ,'posting_end_date'
        ]
    list_filter = [
         'status'
        ,'created_by'
        ,'posting_start_date'
        ,'posting_end_date'
        ,'city'
         ]
    list_select_related = True
    fields = [
         'title'
        ,'posting_end_date'
        ,'status'
        ,'hiring_manager'
        ,'posting_number'
        ,'confidential'
        ,'city'
        ,'candidate_source'
        ,'cost'
        ,'consulting_time'
        ,'posting_sources'
        ,'comments'
        ,'start_date'
        ,'end_date'
        ,'hired_number'
        ,'responsability'
        ,'requirement'
        ]

    def save_model( self, request, obj, form, change ):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
            obj.updated_by = request.user
        obj.save()
 
admin.site.register( Mandate, MandateAdmin )

###############################################################################
class MACAdmin( admin.ModelAdmin ):
    date_hierarchy = 'date'
    list_display = [
         'id'
        ,'candidate'
        ,'mandate'
        ,'date'
        ,'activity'
        ,'status'
        ,'created_by'
        ,'description'
        ]
    list_filter = [
         'date'
        ,'activity'
        ,'status'
        ,'created_by'
        ]
    search_fields = [
         'id'
        ,'candidate__name'
        ,'mandate__title'
        ,'date'
        ,'activity__title'
        ,'status_title'
        ,'created_by__username'
        ,'description'
        ]
    list_select_related = True
    fields = [
         'candidate'
        ,'mandate'
        ,'date'
        ,'activity'
        ,'status'
        ,'description'
        ]

    def save_model( self, request, obj, form, change ):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
            obj.updated_by = request.user
        obj.save()
 
admin.site.register( MAC, MACAdmin)



