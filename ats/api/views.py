import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode
from ats.main.models import *
from ats.settings import *
from ats.api.decorators import *

##decorators####################################################################
login_needed = user_passes_test( lambda u: not u.is_anonymous()
                                ,login_url = '/ats/login/' )

################################################################################
@logged_in_or_basicauth()
@group_required('api')
def mandate_detail( request, mandate ):
    """
    Return the list of mandates with general info 
    """
    today = datetime.date.today()
    querywhere = Q( Q( id = 1 ) , \
                    Q( posting_start_date__lte = today ) , \
                    Q( posting_end_date__gte =  today  ) | \
                    Q( posting_end_date__isnull = True ) 
                  )
 
    queryset = Mandate.objects.filter( querywhere )

    candidate = request.GET.get( 'candidate', '0' )
    if candidate.isdigit() and int( candidate ):
        queryset = queryset.extra( select = 
            { 'get_user_apply' : 
              'SELECT COUNT(1)'\
              ' FROM main_mac'\
              ' WHERE main_mac.mandate_id = main_mandate.id'\
              '  AND  main_mac.candidate_id = %s LIMIT 1' % ( candidate )
            } )
 
    total = len( queryset )

    fields = ( 
         'id'
        ,'title'
        ,'requirement'
        ,'responsability'
        ,'posting_start_date'
        ,'city'
        ,'posting_number'
        )

    #excludes = ( )
    #relations = { }
    extras = ('get_user_apply', )
    #relations = {}

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json'
                                       ,queryset
                                       ,fields = fields
                                       #,excludes = excludes
                                       ,extras = extras
                                       #,relations = relations 
        ) )

    return HttpResponse( data, mimetype = 'application/json' )

################################################################################
@logged_in_or_basicauth()
@group_required('api')
def mandate_list( request ):
    """
    Return the list of mandates with general info 
    In case of user loggin return if applied or not
    """
    #number of return values
    limit = 15
    start = request.GET.get( 'start', '0' )
    if start.isdigit():
        start = int( start )
        limit = start + limit


    candidate = request.GET.get( 'candidate', '0' )
    what = request.GET.get( 'what', '' )
    where = request.GET.get( 'where', '' )

    today = datetime.date.today()
    querywhere = Q( Q( posting_start_date__lte = today ) , \
                 Q( posting_end_date__gte =  today  ) | \
                 Q( posting_end_date__isnull = True  ) )
    for w in what.split():
        if len( w ):
            q = Q( title__icontains = w )
            querywhere = Q( querywhere & q )

    for w in where.split():
        if len( w ):
            q = Q( city__icontains = w )
            querywhere = Q( querywhere & q )

    if candidate.isdigit() and int( candidate ):
        queryset = Mandate.objects.select_related( depth=1 )\
            .filter( querywhere )\
            .extra( select = 
                { 'get_user_apply' : 
                  'SELECT COUNT(1)'\
                  ' FROM main_mac'\
                  ' WHERE main_mac.mandate_id = main_mandate.id'\
                  '  AND  main_mac.candidate_id = %s LIMIT 1' % ( candidate )
                } )
 
        total = len( queryset )
    else:
        total = Mandate.objects.count()
        queryset = Mandate.objects.filter( querywhere )
        total = len( queryset )

    fields = ( 
         'id'
        ,'title'
        ,'posting_start_date'
        ,'city'
        ,'posting_number'
        )

    #excludes = ( )
    #relations = { }
    extras = ('get_user_apply', )
    #relations = {}

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json'
                                       ,queryset[ start:limit ]
                                       ,fields = fields
                                       #,excludes = excludes
                                       ,extras = extras
                                       #,relations = relations 
        ) )

    return HttpResponse( data, mimetype = 'application/json' )

################################################################################
@logged_in_or_basicauth()
@group_required('api')
def mandate_list_candidate( request, candidate ):
    """
    Return the list of mandates with general info 
    """
    mandate_ids = MAC.objects.filter(candidate = candidate)\
        .only('mandate')\
        .order_by('-mandate')\
        .distinct()\
        .values_list('mandate')
 
    today = datetime.date.today()
    querywhere = Q( Q( id__in = mandate_ids ) , \
                    Q( posting_start_date__lte = today ) , \
                    Q( posting_end_date__gte =  today  ) | \
                    Q( posting_end_date__isnull = True ) 
                  )
    queryset = Mandate.objects.filter( querywhere )
 
    total = len( queryset )

    fields = ( 
         'id'
        ,'title'
        ,'posting_start_date'
        ,'city'
        ,'posting_number'
        )

    #excludes = ( )
    #relations = { }
    #extras = ('get_user_apply', )
    #relations = {}

    data = '{"total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json'
                                       ,queryset
                                       ,fields = fields
                                       #,excludes = excludes
                                       #,extras = extras
                                       #,relations = relations 
        ) )

    return HttpResponse( data, mimetype = 'application/json' )


################################################################################
@logged_in_or_basicauth()
@group_required('api')
def mandate_apply( request, mandate=0, candidate=0 ):
    """
    Add a candidate to a mandate, if the candidate is related with the mandate
    then does not do anything.
    """
    user = request.user

    try:
        cand = Candidate.objects.get( pk = candidate )
    except Candidate.DoesNotExist:
        resp = '{ "success": false, "error": "DoesNotExist", "msg": "%s" }' \
               % ( 'Candidate' )
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    try:
        mand = Mandate.objects.get( pk = mandate )
    except Mandate.DoesNotExist:
        resp = '{ "success": false, "error": "%s", "msg": "%s" }' \
               % ( 'DoesNotExist', 'Mandate' )
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    today = datetime.date.today()
    querywhere = Q( Q( candidate = cand ) , \
                    Q( mandate = mand ) , \
                    Q( posting_start_date__lte = today ) , \
                    Q( posting_end_date__gte =  today  ) | \
                    Q( posting_end_date__isnull = True ) 
                  )
 
    queryset = Mandate.objects.filter( querywhere )
    if len( macs ):
        resp = '{ "success": false, "error": "%s", "msg": "%s" }' \
               % ( 'Exists', 'Already apllied' ) 
    else:
        form = MACNewForm( request.POST )
        if form.is_valid():
            object = form.save( commit = False )
            object.created_by = user
            object.candidate = cand
            object.mandate = mand
            object.save()
            resp = '{ "success": true }'
        else:
            resp = '{ "success": false, "error": "%s", "msg": "%s" }' \
                   % ( 'InvalidForm', dict( form.errors.items() ) )
   

    return HttpResponse( resp, mimetype = 'application/json' )

################################################################################
@csrf_exempt
@logged_in_or_basicauth()
@group_required('api')
def candidate_new( request ):
    form = CandidateForm( request.POST )
    user = request.user
    if form.is_valid():
        object = form.save( commit = False )
        object.created_by = user
        object.updated_by = user
        object.save()
        #Generate first MAC for candidate
        mac = MAC(
             created_by = user
            ,updated_by = user
            ,candidate = object
            ,date = datetime.date.today() 
            )
        mac.save()
        #create data directory for candidate
        savepath = os.path.join( MEDIA_ROOT, 'candidate', str( object.id ) )
        if not os.path.exists( savepath ):
            os.mkdir( savepath )
        resp = '{ "success": true, "candidate": %d }' % ( object.id )
    else:
        resp = '{ "success": false, "error": "InvalidForm", "msg": "%s" }' \
               % ( dict(form.errors.items() ) )

    return HttpResponse( resp,
                         mimetype = 'application/json' )

################################################################################
@csrf_exempt
@logged_in_or_basicauth()
@group_required('api')
def candidate_update( request, candidate=0 ):
    try:
        cand = Candidate.objects.get( pk = candidate )
    except Candidate.DoesNotExist:
        resp = '{ "success": false, "error": "DoesNotExist", "msg": "%s" }' \
               % ( 'Candidate' )
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    user = request.user

    if request.POST.has_key( 'first_name' ):
        cand.first_name = request.POST.get('first_name')
    if request.POST.has_key( 'last_name' ):
        cand.last_name = request.POST.get('last_name')
    if request.POST.has_key( 'phone' ):
        cand.phone = request.POST.get('phone','')
    if request.POST.has_key( 'mobile' ):
        cand.mobile = request.POST.get('mobile','')
    if request.POST.has_key( 'email_1' ):
        cand.email_1 = request.POST.get('email_1','')
    cand.save()
    ##Generate MAC for candidate
    mac = MAC(
         created_by = user
        ,updated_by = user
        ,candidate = cand
        ,date = datetime.date.today() 
        )
    mac.save()
    resp = '{ "success": true }'

    return HttpResponse( resp,
                         mimetype = 'application/json' )

################################################################################
@logged_in_or_basicauth()
@group_required('api')
def candidatefile_list( request, candidate ):

    candidate__id = candidate

    #retrieve files for candidate
    if candidate__id.isdigit() and int( candidate__id ):
        queryset = CandidateFile.objects.filter( 
             candidate__id = candidate__id
            ,deleted =  False
            ,created_by = request.user
            )
    else:
        resp = """{ "success" : true, "total": 0, "results" : [] }"""
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    fields = ( 'title'
              ,'created_time'
             )
    
    extras = ('download_link', 'download_name')

    total = len( queryset )
    data = '{ "success": true, "total": %s, "results": %s}' %\
        ( total, serializers.serialize( 'json'
                                       ,queryset
                                       ,fields = fields
                                       ,extras = extras ) )
    return HttpResponse( data
                        ,mimetype = 'application/json' )

#-------------------------------------------------------------------------------
@logged_in_or_basicauth()
@group_required('api')
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
@logged_in_or_basicauth()
@group_required('api')
def candidatefile_del( request, candidate, filename ):
    """ candidate : id
        file: filename
    """

    filepath = os.path.join( 'candidate', str(candidate)
                            ,urllib.url2pathname( filename.encode('utf-8') ) )

    if not FSS.exists( filepath ):
        resp = '{ "success": False, "msg": "File '+filepath+' does not exist" }'
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    #retrieve file object
    candidatefiles = CandidateFile.objects.filter( 
         candidate__id = candidate
        ,created_by = request.user
        ,deleted = False
        ,file = filepath.decode('utf-8')
        )

    #return HttpResponse( filepath, mimetype = 'application/text' )
    if len( candidatefiles ) == 0:
        resp = '{ "success": False, "msg": "File does not exist or not perms" }'
        return HttpResponse( resp
                            ,mimetype = 'application/json' )

    #must be just one file
    candidatefile = candidatefiles[ 0 ]
    response = HttpResponse( candidatefile.file.read() )
    candidatefile.deleted = True
    candidatefile.save()
    resp = """{ success: True } """
             
    response = HttpResponse( resp
                            ,mimetype = 'application/json' )
    #for the Ext.Ajax request
    #response['Content-Type'] = 'text/html'
    return response

#-------------------------------------------------------------------------------
@csrf_exempt
@logged_in_or_basicauth()
@group_required('api')
def candidatefile_new( request, resume = False ):
    """Upload file for candidate
    """
    form = CandidateFileForm( request.POST, request.FILES )
    if form.is_valid():
        try:
            object = form.save( commit=False )
            object.created_by = request.user
            file = request.FILES[ 'file' ]
            object.file.save( file.name, file )
            object.title = file.name 
            object.save()
        except Exception, e:
            resp = '{ success: false, error: "File", msg : "%s" }' % e
            return HttpResponse( resp
                                ,mimetype = 'application/json' )
        resp = '{ success: true }'

        #converting file to txt and saving it to database
        # If the file is PDF then Convert to TEXT file
        filepath = object.file.path.encode('utf-8')
        popen = os.popen( "file -bi "+ filepath, 'r' )
        filetype = popen.read()
        if filetype.startswith('application/pdf'):
            totext_cmd = \
                ' '.join( [ "/usr/bin/pdftotext -htmlmeta -layout -enc UTF-8"
                           ,filepath
                           ,'-' ] )
            popen = os.popen( totext_cmd )
            object.txt = smart_str( popen.read() )
            object.save()
            if resume:
                object.candidate.resume = object.txt
                object.candidate.save()
        elif filetype.startswith('application/vnd.ms-office'):
            totext_cmd = ' '.join( [ "/usr/bin/catdoc -w -dUTF-8"
                                    ,filepath ] )
            popen = os.popen( totext_cmd )
            object.txt = smart_str( popen.read() )
            object.save()
            if resume:
                object.candidate.resume = object.txt
                object.candidate.save()
    else:
        resp = '{ success: false, error: "InvalidForm", msg: "%s" }' \
               % ( dict(form.errors.items() ) )

    response = HttpResponse( resp
                            ,mimetype = 'application/json' )

    #ExtJs return for fileUpload field
    if request.is_ajax():
        response['Content-Type'] = 'text/html'

    return response
    
