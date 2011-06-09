import os, sys
import datetime
import re

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from ats.common.decorators import login_needed, group_required
from ats.main.models import *
from ats.main.forms import *

################################################################################
@login_needed
def index( request ):
    c = {
            'user': request.user,
        }
    return render_to_response( 'main/templates/index.html', c )


#CANDIDATE######################################################################
@login_needed
@group_required('recruiter')
def candidate_queryset( request ):
    start = int( request.REQUEST.get( 'start', 0 ) )
    limit = 15
    #limit = int( request.REQUEST.get( 'limit', 15 ) )

    #sorting
    orderby = request.REQUEST.get( 'sort', 'id' ).strip()
    dir = request.REQUEST.get( 'dir', 'ASC' ).strip()
    if dir == 'DESC':
        orderby = "-%s" % ( orderby ) 

    #quicksearch
    query = request.REQUEST.get( 'query', '').strip().split()
    querywhere = Q()

    #SPECIFIC SEARCH
    if request.REQUEST.has_key( 'candidate__id'):
        qcandidate__id =  request.REQUEST.get( 'candidate__id', '').strip()
        if qcandidate__id.isdigit():
            query.append( 'candidate='+qcandidate_id )
    
    if request.REQUEST.get( 'mandate__id'):
        qmandate__id=  request.REQUEST.get( 'mandate__id', '').strip()
        if qmandate__id.isdigit():
            query.append( 'mandate='+qmandate__id )


    #advance search
    for x in query:
        if len( x.split("=") ) == 2:
            field, value = x.split("=")
            if field == 'mandate' and value.isdigit():
                candidate_ids = MAC.objects.filter(mandate = value)\
                    .only('candidate')\
                    .order_by('-candidate')\
                    .distinct()\
                    .values_list('candidate')
                querywhere = Q( querywhere & Q(id__in = candidate_ids ) )
            elif field == 'candidate' and value.isdigit():
                querywhere = Q( querywhere & Q(id = value ) )
  
    #general search
    for x in query:
        if len( x ) and len( x.split("=") ) != 2:
            q = Q( Q(first_name__icontains=x)
                  |Q(last_name__icontains=x)
                  |Q(phone__icontains=x)
                  |Q(mobile__icontains=x)
                  |Q(email_1__icontains=x)
                  |Q(created_by__username__iexact=x)
                 )
            querywhere = Q( querywhere & q )

    total = Candidate.objects.filter( querywhere ).count()

    queryset = Candidate.objects.select_related( depth=1 )\
        .filter( querywhere )\
        .order_by( orderby )

    return total, queryset[ start : start + limit ]

#-------------------------------------------------------------------------------
@login_needed
@group_required('recruiter')
def candidate_list( request ):
    total , queryset = candidate_queryset( request )
    excludes = ()

    relations = {
                    'created_by': 
                    {
                        'fields': ('username',)
                    }
                    ,'updated_by': 
                    {
                        'fields': ('username',)
                    }
                    ,'professional_designations':
                    {
                        'fields': ('id','title',)
                    }
                     ,'managment_experience':
                    {
                        'fields': ('id','title',)
                    }
                     ,'work_locations':
                    {
                        'fields': ('id','title',)
                    }
                     ,'work_types':
                    {
                        'fields': ('id','title',)
                    }
                }

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize('json', 
                                       queryset, 
                                       excludes = excludes,
                                       relations = relations ) )
    return HttpResponse( data, mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@login_needed
@group_required('recruiter')
def candidate_list_combobox( request ):
    start = int( request.REQUEST.get( 'start', 0 ) )
    limit = int( request.REQUEST.get( 'limit', 15 ) )
    query = request.REQUEST.get( 'query', '').strip()

    querywhere = Q()
    for x in query.split():
        if len( x ):
            q = Q( Q(first_name__icontains=x)
                  |Q(last_name__icontains=x) )
            if x.isdigit():
                q = Q( q | Q( id = int( x ) ) )
            querywhere = Q( querywhere & q )
    
    total = Candidate.objects.filter( querywhere ).count()
    queryset = Candidate.objects.filter( querywhere )\
        .order_by( 'first_name', 
                   'last_name' )
    fields = ('id',
              'first_name',
              'last_name' )

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize('json', 
                                       queryset[start:start+limit], 
                                       fields = fields) )
    return HttpResponse( data, mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def candidate_update( request, form_type  ):
    id = request.POST.get( 'id', None )
    if id is None or len( id.strip() ) == 0:
        return HttpResponse('{ success: false,\
                               error: "DoesNotExists",\
                               msg: "The candidate to update is null" }',
                            mimetype = 'application/json')

    try:
        object = Candidate.objects.get( pk = id )
    except Candidate.DoesNotExist:
        return HttpResponse('{ success: false,\
                               error: "DoesNotExists",\
                               msg: "The candidate to update does not exists"}',
                            mimetype = 'application/json' ) 

    #Cleaning ManyToMany to pass is _valid
    data = request.POST.copy()
    if data.has_key('professional_designations')\
       and len( data['professional_designations'] ) == 0:
        data.pop('professional_designations')
    if data.has_key('work_types') and len( data['work_types'] ) == 0:
        data.pop('work_types')
    if data.has_key('work_locations') and len( data['work_locations'] ) == 0:
        data.pop('work_locations')

    #form_type = request.POST.get( 'form' )
    if form_type == 'personal':
        form = CandidatePersonalEditForm( data, instance = object )
    elif form_type == 'experience':
        form = CandidateExperienceEditForm( data, instance = object )
    else:
        return HttpResponse('{ success: false,\
                               error: "DoesNotExists",\
                               msg: "The form to update does not exists"}',
                            mimetype = 'application/json' )
        #general update saving user
        #form = CandidateForm( data, instance = object )

    if form.is_valid():
        object = form.save( commit = False)
        object.updated_by = request.user
        object.save()
        form.save_m2m()
        return HttpResponse( '{ success: true }'
                            ,mimetype = 'application/json' )
    else:
        msg = '{ success: false, error: "InvalidForm", msg: "%s" }' \
              % ( dict( form.errors.items() ) )
        return HttpResponse( msg
                            ,mimetype = 'application/json')

#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def candidate_new( request ):
    form = CandidateForm( request.POST )
    if form.is_valid():
        object = form.save( commit = False )
        object.created_by = request.user
        object.updated_by = request.user
        object.save()
        #Generate first MAC for candidate
        mac = MAC(
             created_by = request.user
            ,updated_by = request.user
            ,candidate = object
            ,date = datetime.date.today() 
            ,description = 'New candidate' 
            )
        mac.save()
        #create data directory for candidate
        savepath = os.path.join( MEDIA_ROOT, 'candidate', str( object.id ) )
        if not os.path.exists( savepath ):
            os.mkdir( savepath )
        resp = '{ success: true }'
    else:
        resp = '{ success: false, error: "InvalidForm", msg: "%s" }' \
               % ( dict(form.errors.items() ) )

    return HttpResponse( resp,
                         mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@login_needed
@group_required('recruiter')
def candidatefile_get( request, candidate, filename ):
    """ candidate : id
        file: filename
    """

    filepath = os.path.join( 'candidate'
                            , str(candidate) 
                            , urllib.url2pathname( filename.encode('utf-8') ) )

    if not FSS.exists( filepath ):
        resp = '{ "success": False, "msg": "File does not exist" }'
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    #retrieve file object
    candidatefiles = CandidateFile.objects.filter( 
         candidate__id = candidate
        ,deleted = False
        ,file = filepath.decode('utf-8')
        )

    #return HttpResponse( filepath, mimetype = 'application/text' )
    if len( candidatefiles ) == 0:
        resp = '{ "success": False, "msg": "File %s not found" }' % filepath
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    #must be just one file
    candidatefile = candidatefiles[ 0 ]
    response = HttpResponse( candidatefile.file.read() )
    response['Content-Disposition'] = 'attachment; filename="%s"' % \
        ( urllib.url2pathname( candidatefile.title.encode( 'utf-8' ) ), )
    return  response

#-------------------------------------------------------------------------------
@login_needed
@group_required('recruiter')
def candidatefile_list( request ):
    candidate__id = request.REQUEST.get('candidate__id', '0')

    #retrieve files for candidate
    if candidate__id.isdigit() and int( candidate__id ):
        queryset = CandidateFile.objects.filter( 
             candidate__id = candidate__id
            ,deleted =  False
            )
    else:
        resp = """{ "total": 0, "results" : [] }"""
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    fields = ( 'title'
              ,'created_time'
              ,'created_by' )
    
    extras = ('download_link',)
    total = len( queryset )
    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json'
                                       ,queryset
                                       ,fields = fields
                                       ,extras = extras ) )
    return HttpResponse( data
                        ,mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def candidatefile_del( request ):
    """ candidatefile: id 
    """
    id = request.POST.get('id','0')

    if id.isdigit() and int( id ):
        try:
            file = CandidateFile.objects.get( pk = id )
            file.deleted = True
            file.save()
            resp = """{ success: true } """
        except DoesNotExist:
            resp = """{ success: false, error: "DoesNotExist" } """
             
    response = HttpResponse( resp
                            ,mimetype = 'application/json' )
    #for the Ext.Ajax request
    response['Content-Type'] = 'text/html'
    return response
#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def candidatefile_new( request ):
    """ candidate: id 
    """

    form = CandidateFileForm( request.POST, request.FILES )
    if form.is_valid():
        object = form.save( commit=False )
        object.created_by = request.user
        file = request.FILES[ 'file' ]
        object.file.save( file.name, file )
        object.title = file.name 
        object.save()
        resp = '{ success: true }'
    else:
        resp = '{ success: false, error: "InvalidForm", msg: "%s" }' \
               % ( dict(form.errors.items() ) )

    response = HttpResponse( resp
                            ,mimetype = 'application/json' )

    #ExtJs return for fileUpload field
    response['Content-Type'] = 'text/html'
    return response

#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def candidatefile_resume( request ):
    id = request.POST.get('id','0')
    candidate__id = request.POST.get('candidate__id','0')

    if id.isdigit() and int( id ) and\
       candidate__id.isdigit() and int( candidate__id ):
        #try:
        candidatefile = CandidateFile.objects.get( pk = id )
        candidate = Candidate.objects.get( pk = candidate__id )
        candidate.resume = file2txt( candidatefile.file.path )
        candidate.save()
        resp = """{ success: true } """
        #except:
            #except DoesNotExist:
        #    resp = """{ success: false, error: "DoesNotExist" } """
             
    response = HttpResponse( resp
                            ,mimetype = 'application/json' )
    #for the Ext.Ajax request
    response['Content-Type'] = 'text/html'
    return response


def file2txt( path ):
    #converting file to txt and saving it to database
    # If the file is PDF then Convert to TEXT file
    popen = os.popen( "file -bi "+ path, 'r' )
    filetype = popen.read()
    if filetype.startswith('application/pdf'):
        totext_cmd = \
            ' '.join( [ "/usr/bin/pdftotext -htmlmeta -layout -enc UTF-8"
                       ,path
                       ,'-' ] )
        popen = os.popen( totext_cmd )
        return popen.read()
    elif filetype.startswith('application/vnd.ms-office'):
        totext_cmd = ' '.join( [ "/usr/bin/catdoc -w -dUTF-8"
                                ,path ] )
        popen = os.popen( totext_cmd )
        return popen.read()
    else:
        return 'File was not possible to convert' 

#MANDATE########################################################################
@login_needed
@group_required('recruiter')
def mandate_queryset( request ):
    start = int( request.POST.get( 'start', 0 ) )
    limit = 15
    #limit = int( request.POST.get( 'limit', 15 ) )

    #sorting
    orderby = request.REQUEST.get( 'sort', 'id' ).strip()
    dir = request.REQUEST.get( 'dir', 'ASC' ).strip()
    if dir == 'DESC':
        orderby = "-%s" % ( orderby ) 

    #QUICKSEARCH
    query = request.REQUEST.get( 'query', '').strip().split()
    querywhere = Q()
    
    #advance search
    for x in query:
        if len( x.split("=") ) == 2:
            field, value = x.split("=")
            if field == 'candidate' and value.isdigit():
                mandate_ids = MAC.objects.filter(candidate = value)\
                    .only('mandate')\
                    .order_by('-mandate')\
                    .distinct()\
                    .values_list('mandate')
                querywhere = Q( querywhere & Q(id__in = mandate_ids ) )
            elif field == 'mandate' and value.isdigit():
                querywhere = Q( querywhere & Q(id = value ) )
 
    #general search
    for x in query:
        #jump strings from advance search
        if len( x ) and len( x.split("=") ) != 2:
            q = Q( Q(title__icontains=x)
                  |Q(status__title__icontains=x)
                  |Q(hiring_manager__name__icontains=x)
                  |Q(responsability__icontains=x)
                  |Q(requirement__icontains=x)
                  |Q(city__icontains=x)
                  |Q(created_by__username__iexact=x)
                 )
            querywhere = Q( querywhere, q )

            try:
                xs = x.split('-')
                x = datetime.date( int(xs[0]), int(xs[1]), int(xs[2]) )
                q = q | Q( posting_end_date = x )
            except:
                pass

            querywhere = Q( querywhere & q )
    
    total = Mandate.objects.filter( querywhere ).count()

    #extra fields added: candidate_count
    queryset = Mandate.objects.select_related( depth=1 )\
        .extra( select = 
            { 'candidate_count' : 
              'SELECT COUNT(DISTINCT main_mac.candidate_id) FROM main_mac'\
              ' WHERE main_mac.mandate_id = main_mandate.id' } )\
        .filter( querywhere )\
        .order_by( orderby )

    return total, queryset[ start : start + limit ]

#-------------------------------------------------------------------------------
@login_needed
@group_required('recruiter')
def mandate_list( request ):
    total , queryset = mandate_queryset( request )
    excludes = ('updated_by',
                'updated_time',
                'created_time')

    relations = {
                    'created_by': 
                    {
                        'fields': ('username',)
                    },
                    'status': 
                    {
                        'fields': ('id','title')
                    },
                    'hiring_manager': 
                    {
                        'fields': ('id','name',)
                    }
                }

    extras = ('candidate_count',)

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize('json', 
                                       queryset, 
                                       excludes = excludes,
                                       extras = extras,
                                       relations = relations ) )
    return HttpResponse( data, mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@login_needed
@group_required('recruiter')
def mandate_list_combobox( request ):
    start = int( request.REQUEST.get( 'start', 0 ) )
    limit = int( request.REQUEST.get( 'limit', 15 ) )
    query = request.REQUEST.get( 'query', '').strip()

    
    querywhere = Q()
    #case when asking for strings
    for x in query.split():
        if len( x ):
            q = Q(title__icontains=x)
            if x.isdigit():
                q = Q( q | Q( id = int( x ) ) )
            querywhere = Q( querywhere & q )
    
    total = Mandate.objects.filter( querywhere ).count()
    queryset = Mandate.objects.filter( querywhere )\
        .order_by( 'title' )
    fields = ('id',
              'title' )

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize('json', 
                                       queryset, 
                                       fields = fields) )
    return HttpResponse( data, mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def mandate_update( request ):
    id = request.POST.get( 'id', None )
    if id is None or len( id.strip() ) == 0:
        return HttpResponse('{ success: false,\
                               error: "DoesNotExists",\
                               msg: "The mandate to update is null" }',
                            mimetype = 'application/json')

    try:
        object = Mandate.objects.get( pk = id )
    except Mandate.DoesNotExist:
        return HttpResponse('{ success: false,\
                               error: "DoesNotExists",\
                               msg: "The mandate to update does not exists"}',
                            mimetype = 'application/json' ) 

    #general update saving user
    form_type = request.POST.get( 'form' )
    if form_type == 'mandateeditform':
        form = MandateEditForm(
             request.POST
            ,instance = object )
    elif form_type == 'mandaterequirementform':
        form = MandateRequirementForm( 
             request.POST 
            ,instance = object )
    elif form_type == 'mandateresponsabilityform':
        form = MandateResponsabilityForm( 
             request.POST 
            ,instance = object )
    elif form_type == 'mandateclosingform':
        form = MandateClosingForm( 
             request.POST 
            ,instance = object )
    else:
        form = None

    if form is None:
        msg = '{ success: false, error: "InvalidForm", msg: "%s" }' \
              % ( 'Form to validate does not exits', )
    elif form.is_valid():
        object = form.save( commit = False )
        object.updated_by = request.user
        object.save()
        form.save_m2m()
        msg = '{ success: true, msg: "Mandate updated" }'
    else:
        msg = '{ success: false, error: "InvalidForm", msg: "%s" }' \
              % ( dict(form.errors.items() ) )
    
    return HttpResponse( msg,
                         mimetype = 'application/json')

#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def mandate_new( request ):
    form = MandateForm( request.POST )
    if form.is_valid():
        object = form.save( commit = False )
        object.created_by = request.user
        object.save()
        #Generate first MAC for mandate
        mac = MAC(
             created_by = request.user
            ,updated_by = request.user
            ,mandate = object
            ,date = datetime.date.today() 
            ,description = 'New mandate' 
            )
        mac.save()
        return HttpResponse('{ success: true }',
                            mimetype = 'application/json' ) 
    else:
        msg = '{ success: false, error: "InvalidForm", msg: "%s" }' \
              % ( dict(form.errors.items() ) )

        return HttpResponse( msg,
                             mimetype = 'application/json' )

#-------------------------------------------------------------------------------
#MAC############################################################################
@login_needed
@group_required('recruiter')
def mac_queryset( request ):
    start = int( request.REQUEST.get( 'start', 0 ) )
    limit = 15
    #limit = int( request.REQUEST.get( 'limit', 15 ) )

    #sorting
    orderby = request.REQUEST.get( 'sort', 'id' ).strip()
    dir = request.REQUEST.get( 'dir', 'ASC' ).strip()
    if dir == 'DESC':
        orderby = "-%s" % ( orderby ) 

    #SEARCH
    querywhere = Q()

    #SPECIFIC SEARCH
    if request.REQUEST.has_key('candidate__id'):
        qcandidate__id =  request.REQUEST.get( 'candidate__id').strip()
        if qcandidate__id.isdigit():
            querywhere = Q( querywhere & Q( candidate__id = qcandidate__id ) )
    
    if request.REQUEST.has_key('mandate__id'):
        qmandate__id = request.REQUEST.get( 'mandate__id').strip()
        if qmandate__id.isdigit():
            querywhere = Q( querywhere & Q( mandate__id = qmandate__id) )
    #extra filter
    if request.REQUEST.has_key('date<='):
        querywhere = Q( querywhere & Q( date__lte = request.REQUEST.get('date<=').strip() ) ) 
    if request.REQUEST.has_key('date>='):
        querywhere = Q( querywhere & Q( date__gte = request.REQUEST.get('date>=').strip() ) ) 
    #option panel
    if request.REQUEST.has_key('candidates'):
        querywhere = Q( querywhere & \
                        Q( candidate__id__in = \
                           request.REQUEST.get('candidates').strip().split(",") ) ) 
    if request.REQUEST.has_key('mandates'):
        querywhere = Q( querywhere & \
                        Q( mandate__id__in = \
                           request.REQUEST.get('mandates').strip().split(",") ) ) 
    if request.REQUEST.has_key('statues'):
        querywhere = Q( querywhere & \
                        Q( status__id__in = \
                           request.REQUEST.get('statues').strip().split(",") ) ) 
    if request.REQUEST.has_key('activities'):
        querywhere = Q( querywhere & \
                        Q( activity__id__in = \
                           request.REQUEST.get('activities').strip().split(",") ) ) 
    if request.REQUEST.has_key('description'):
        querywhere = Q( querywhere & \
                        Q( description__icontains = \
                           request.REQUEST.get('description').strip() ) ) 



    #QUICKSEARCH
    query = request.REQUEST.get( 'query', '').strip().split()
    
    #advance search
    query_list_general = []
    for x in query:
        m = re.match('date=(?P<date>\d{4}\-\d{2}\-\d{2})', x)
        if m:
            querywhere = Q( querywhere & Q( date = m.group( 'date' ) ) )
            continue
        m = re.match('date<(?P<date>\d{4}\-\d{2}\-\d{2})', x)
        if m:
            querywhere = Q( querywhere & Q( date__lt = m.group( 'date' ) ) )
            continue
        m = re.match('date<=(?P<date>\d{4}\-\d{2}\-\d{2})', x)
        if m:
            querywhere = Q( querywhere & Q( date__lte = m.group( 'date' ) ) )
            continue
        m = re.match('date>(?P<date>\d{4}\-\d{2}\-\d{2})', x)
        if m:
            querywhere = Q( querywhere & Q( date__gt = m.group( 'date' ) ) )
            continue
        m = re.match('date>=(?P<date>\d{4}\-\d{2}\-\d{2})', x)
        if m:
            querywhere = Q( querywhere & Q( date__gte = m.group( 'date' ) ) )
            continue
        m = re.match('candidate=(?P<id>\d+)', x)
        if m:
            querywhere = Q( querywhere & Q(candidate__id = m.group( 'id' ) ) )
            continue
        m = re.match('mandate=(?P<id>\d+)', x)
        if m:
            querywhere = Q( querywhere & Q( mandate__id = m.group( 'id' ) ) )
            continue
        m = re.match('mac=(?P<id>\d+)', x)
        if m:
            querywhere = Q( querywhere & Q( id = m.group( 'id' ) ) )
            continue
        if len( x ):
            query_list_general.append( x )

    #general search
    for x in query_list_general:
        q = Q( Q(description__icontains=x)
              |Q(mandate__title__icontains=x)
              |Q(candidate__first_name__icontains=x)
              |Q(candidate__last_name__icontains=x)
              |Q(status__title__iexact=x)
              |Q(activity__title__iexact=x)
              |Q(created_by__username__iexact=x)
             )
        try:
            m = re.match('(?P<date>\d{4}\-\d{2}\-\d{2})', x)
            if m:
                q = q | Q( date = x )
        except:
            pass
        
        querywhere = Q( querywhere & q )
    
    total = MAC.objects.filter( querywhere ).count()

    queryset = MAC.objects.select_related( depth=1 )\
        .filter( querywhere )\
        .order_by( orderby )

    return total, queryset[ start : start + limit ]

#-------------------------------------------------------------------------------
@login_needed
@group_required('recruiter')
def mac_list( request ):
    total , queryset = mac_queryset( request )
    excludes = ('updated_by',
                'updated_time',
                'created_time')

    relations = {
                    'created_by': 
                    {
                        'fields': ('username',)
                    }
                    ,'status': 
                    {
                        'fields': ('title',)
                    }
                    ,'activity': 
                    {
                        'fields': ('title',)
                    }
                    ,'candidate': 
                    {
                        'fields': ( 'first_name'
                                   ,'last_name'
                                   ,'phone'
                                   ,'phone_extension'
                                   ,'mobile' )
                    }
                    ,'mandate': 
                    {
                        'fields': ('title',)
                    }
                }

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize('json', 
                                       queryset, 
                                       excludes = excludes,
                                       relations = relations ) )
    return HttpResponse( data, mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def mac_update( request ):
    id = request.POST.get( 'id', None )
    if id is None or len( id.strip() ) == 0:
        resp = '{ success: false,\
                  error: "DoesNotExists",\
                  msg: "The MAC to update is null" }'
        return HttpResponse( resp
                            ,mimetype = 'application/json')

    try:
        object = MAC.objects.get( pk = id )
    except MAC.DoesNotExist:
        resp = '{ success: false,\
                  error: "DoesNotExists",\
                  msg: "The MAC to update does not exists"}'
        return HttpResponse( resp
                            ,mimetype = 'application/json' ) 

    #general update saving user
    form = MACUpdateForm( request.POST, instance = object )
    if form.is_valid():
        object = form.save( commit = False)
        object.updated_by = request.user
        object.save()
        resp = '{ success: true }',
    else:
        resp = '{ success: false, error: "InvalidForm", msg: "%s" }' \
              % ( dict( form.errors.items() ) )
    
    return HttpResponse( resp,
                         mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@csrf_exempt
@login_needed
@group_required('recruiter')
def mac_new( request ):
    form = MACNewForm( request.POST )
    if form.is_valid():
        object = form.save( commit = False )
        object.created_by = request.user
        object.save()
        resp = '{ success: true }'
    else:
        resp = '{ success: false, error: "InvalidForm", msg: "%s" }' \
               % ( dict(form.errors.items() ) )

    return HttpResponse( resp
                        ,mimetype = 'application/json' )

#-------------------------------------------------------------------------------





