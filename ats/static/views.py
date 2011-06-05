from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, Http404
from django.core import serializers
from django.db.models import Q
from ats.static.models import *

##decorators####################################################################
login_needed = user_passes_test( lambda u: not u.is_anonymous()
                                ,login_url = '/ats/login/' )

#ACTIVITY#######################################################################
#@login_needed
def activity_list( request ):
    total = Activity.objects.count()
    queryset = Activity.objects\
        .filter( Q( priority__isnull = False ) )\
        .order_by('priority','title')

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json', 
                                        queryset ) )
    return HttpResponse( data
                        ,mimetype = 'application/json' )


#MACSTATUS######################################################################
#@login_needed
def mac_status_list( request ):
    total = MACStatus.objects.count()
    queryset = MACStatus.objects\
        .filter( Q( priority__isnull = False ) )\
        .order_by('priority','title')

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json', 
                                        queryset ) )
    return HttpResponse( data, mimetype = 'application/json' )

#MANDATESTATUS##################################################################
#@login_needed
def mandate_status_list( request ):
    total = MandateStatus.objects.count()
    queryset = MandateStatus.objects\
        .filter( Q( priority__isnull = False ) )\
        .order_by('priority','title')

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json', 
                                        queryset ) )
    return HttpResponse( data, mimetype = 'application/json' )

#HIRING MANAGER#################################################################
@login_needed
def hiring_manager_list( request ):
    total = HiringManager.objects.count()
    queryset = HiringManager.objects\
        .filter( Q( priority__isnull = False ) )\
        .order_by('priority','name')

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json', 
                                        queryset ) )
    return HttpResponse( data, mimetype = 'application/json' )

#PROFESSIONAL DESIGNATION#######################################################
@login_needed
def professional_designation_list( request ):
    total = ProfessionalDesignation.objects.count()
    queryset = ProfessionalDesignation.objects\
        .filter( Q( priority__isnull = False ) )\
        .order_by('priority','title')

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json', 
                                        queryset ) )
    return HttpResponse( data, mimetype = 'application/json' )

#MANAGMENT EXPERIENCE###########################################################
@login_needed
def managment_experience_list( request ):
    total = ManagmentExperience.objects.count()
    queryset = ManagmentExperience.objects\
        .filter( Q( priority__isnull = False ) )\
        .order_by('priority','title')

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json', 
                                        queryset ) )
    return HttpResponse( data, mimetype = 'application/json' )

#WORK LOCATION##################################################################
@login_needed
def work_location_list( request ):
    total = WorkLocation.objects.count()
    queryset = WorkLocation.objects\
        .filter( Q( priority__isnull = False ) )\
        .order_by('priority','title')

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json', 
                                        queryset ) )
    return HttpResponse( data, mimetype = 'application/json' )

#WORK TYPE######################################################################
@login_needed
def work_type_list( request ):
    total = WorkType.objects.count()
    queryset = WorkType.objects\
        .filter( Q( priority__isnull = False ) )\
        .order_by('priority','title')

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json', 
                                        queryset ) )
    return HttpResponse( data, mimetype = 'application/json' )

################################################################################
