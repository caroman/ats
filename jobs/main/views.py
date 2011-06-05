import math
import urllib, urllib2, base64
import simplejson

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.utils.encoding import smart_str, smart_unicode

#from profiles import views as profile_views
from jobs.main.models import *
from jobs.main.forms import ProfileForm, UploadCVFileForm, UploadOtherFileForm
from jobs.settings import ATS_REALM, ATS_URI, ATS_USER, ATS_PASSWD


################################################################################
login_needed = user_passes_test(lambda u: not u.is_anonymous(), 
                                login_url='/jobs/login/')

def user_sync_with_ats( user ):
    if user:
        return user.profile_set.all()[0].is_sync()
    return False

user_sync = user_passes_test( lambda u: user_sync_with_ats( u ),
                              login_url = '/jobs/accounts/profile/')

################################################################################
# Use of Basic HTTP Authentication
# Create an OpenerDirector with support for Basic HTTP Authentication..
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
opener = register_openers()
from jobs.bitten.compat import HTTPBasicAuthHandler
auth_handler = HTTPBasicAuthHandler()
auth_handler.add_password(realm = ATS_REALM,
                          uri = ATS_URI,
                          user = ATS_USER,
                          passwd = ATS_PASSWD )
opener.add_handler(auth_handler)
## ...and install it globally so it can be used with urlopen.
raw = "%s:%s" % (ATS_USER, ATS_PASSWD) 
opener.addheaders.append( ( 'Www-Authorization'
                           ,'Basic %s' % base64.b64encode(raw).strip() ) )

################################################################################
def search( request ):
    """
    Request to ATS for all available mandates
    if the candidate is given will return if the user
    has previously applied to the mandate
    """
    url = '/'.join( [ ATS_URI, 'mandate/list/' ] )
    #get start item from page number
    limit = 15 #same as in ats

    page = request.GET.get( 'page', '0' )
    if page.isdigit() and int( page ):
        page = int( page )
    else:
        page = 1
 
    get = {}
    get['start'] = (page-1) * limit 
    what = request.GET.get( 'what', 'what' )
    where = request.GET.get( 'where', 'where' )

    #from django.utils.encoding import smart_str, smart_unicode
    if what != 'what':
        get['what'] = smart_str( what )
        #get['what'] =  what 
    if where != 'where':
        get['where'] = smart_str( where )
        #get['where'] = where

    if not request.user.is_anonymous():
        try:
            profile = Profile.objects.get( user = request.user )    
            if profile.is_sync():
                get['candidate'] = profile.atsid
        except Profile.DoesNotExist:
            pass 
    
    encoded_get = urllib.urlencode( get )
    if len( encoded_get ):
        url+='?%s' % encoded_get

    #REQUEST TO ATS
    r = urllib2.Request( url )
    y = urllib2.urlopen( r )
    read = y.read()
    y.close()
    mandates = simplejson.loads( read )
    #END REQUEST

    #setting page numbers
    if mandates['total'] > limit:
        page_numbers = {
            'previous': page - 1
           ,'current': page
           ,'next': page + 1
           ,'total': int( math.ceil( 1.0*mandates['total']/limit ) )
        }
        if page_numbers['current'] == page_numbers['total']:
            page_numbers['next'] = 0
    else:
         page_numbers = {
            'previous': 0
           ,'current': 1
           ,'next': 0
           ,'total': 1
        }
        

    c = {
             'user': request.user
            ,'mandates':  mandates
            ,'what':  what
            ,'where':  where
            ,'page_numbers':  page_numbers
        }
    return render_to_response( 'main/templates/jobs.html', c )

################################################################################
@login_needed
@user_sync
def user_applications( request ):
    """
    Request to ATS for all available mandates
    if the candidate is given will return if the user
    has previously applied to the mandate
    """

    url = '/'.join( [ ATS_URI, 'mandate/list/candidate/%s/' ] )

    profile = Profile.objects.get( user = request.user )    
    
    #REQUEST TO ATS
    r = urllib2.Request( url % profile.atsid )
    y = urllib2.urlopen( r )
    mandates = y.read()
    y.close()
    simplejson.loads( mandates )
    #END REQUEST

    c = {
             'user': request.user
            ,'mandates': simplejson.loads( mandates )
        }
    return render_to_response( 'main/templates/applications.html', c )

#def create_profile( request ):
#  return profile_views.create_profile( request, form_class=ProfileForm )


#def edit_profile( request ):
#    return profile_views.edit_profile( request, form_class=ProfileForm,
#                                       success_url='/jobs/profiles/sync/' )

################################################################################
@login_needed
def profile_sync( request ):
    profile = Profile.objects.get( user = request.user ) 
    data_encoded = urllib.urlencode( [
              ( 'first_name', smart_str( profile.first_name ) )
             ,( 'last_name', smart_str( profile.last_name ) )
             ,( 'phone', smart_str( profile.phone ) )
             ,( 'mobile', smart_str( profile.mobile ) )
             ,( 'email_1', smart_str( profile.email ) )
        ] )


    if profile.atsid: 
        url = '/'.join( [ ATS_URI, 'candidate/%s/update/' ] )
        r = urllib2.Request( url % ( profile.atsid ), data = data_encoded )
        y = urllib2.urlopen( r )
        #response = y.read()
        #y.close()
        #result = simplejson.loads( response )
    else:
        url = '/'.join( [ ATS_URI, 'candidate/new/' ] )
        r = urllib2.Request( url, data = data_encoded )
        y = urllib2.urlopen( r )
        response = y.read()
        y.close()
        result = simplejson.loads( response )
        profile.atsid = result['candidate']
        profile.save()
 
    return HttpResponseRedirect( '/jobs/' )
                

################################################################################
def detail( request, job=0 ):
    """
    Send the Id of a job, get the object
    and then displayed on a HTML page
    """
    url = '/'.join( [ ATS_URI, 'mandate/%s/' ] )

    if not request.user.is_anonymous():
        try:
            profile = Profile.objects.get( user = request.user )    
            if profile.is_sync():
                url+='?candidate=%s' % profile.atsid
        except Profile.DoesNotExist:
            pass

    #REQUEST
    r = urllib2.Request( url % job )
    y = urllib2.urlopen( r )
    response = y.read()
    y.close()
    mandates = simplejson.loads( response )
    #ENDREQUEST

    if len( mandates['results'] ):
        mandate = mandates['results'][0]
    else:
        mandate = { }
              
    c = { 
          'user': request.user
         ,'mandate' : mandate 
        }
    c.update( csrf( request ) )
    return render_to_response( "main/templates/job.html",
                               c )

################################################################################
@login_needed
@user_sync
def apply( request, job=0 ):
    """
    Apply to a Job
    """

    profile = Profile.objects.get( user = request.user )

    url = '/'.join( [ ATS_URI, 'mandate/%s/apply/%s/' ] )

    r = urllib2.Request( url % ( job, profile.atsid  ) )
    y = urllib2.urlopen( r )
    read = y.read()
    y.close()
    response = simplejson.loads( read )

    if response['success']:
        c = { 'success' : True }
    else:
        c = { 'success' : False }
        c = { 'msg' : response['msg'] }

    c['job'] = job
    c['user'] = request.user
    c.update( csrf( request ) )
    return render_to_response( "main/templates/job_sent.html", c )


################################################################################
@login_needed
@user_sync
def user_files( request ):
    """ Get files from ATS"""

    profile = Profile.objects.get( user = request.user )

    url = '/'.join( [ ATS_URI, 'candidate/%s/file/list/' ] )

    #REQUEST TO ATS
    r = urllib2.Request( url % profile.atsid )
    y = urllib2.urlopen( r )
    read = y.read()
    y.close()
    response = simplejson.loads( read )
    #END REQUEST

    cvfileform = UploadCVFileForm()
    otherfileform = UploadOtherFileForm()
    if response['success']:
        c = {
             'success' : True 
            ,'user': request.user
            ,'files': response
            }
    else:
        c = {
             'success' : False
            ,'msg' : reponse['msg'] 
            }

    c.update( csrf( request ) )
    return render_to_response( 'main/templates/files.html', c )

 
################################################################################
@login_needed
@user_sync
def userfile_get( request, filename ):
    """ 
        Get filename 
    """

    profile = Profile.objects.get( user = request.user )

    url = '/'.join( [ ATS_URI, 'candidate/%s/file/get/%s' ] )

    #REQUEST TO ATS
    filename_encoded = urllib.pathname2url( filename )
    r = urllib2.Request( url % ( profile.atsid, filename_encoded ) )
    y = urllib2.urlopen( r )
    read = y.read()
    y.close()
    ##END REQUEST

    response = HttpResponse( read )
    response['Content-Disposition'] = y.headers["Content-Disposition"]
    return  response

################################################################################
@login_needed
@user_sync
def userfile_del( request, filename ):
    """ 
        Del filename 
    """

    profile = Profile.objects.get( user = request.user )

    url = '/'.join( [ ATS_URI, 'candidate/%s/file/del/%s' ] )

    #REQUEST TO ATS
    filename_encoded = urllib.pathname2url( filename.encode('utf-8') )
    r = urllib2.Request( url % ( profile.atsid, filename_encoded ) )
    y = urllib2.urlopen( r )
    read = y.read()
    y.close()
    ##END REQUEST

    #return  HttpResponse( read )

    return user_files( request )


################################################################################
@login_needed
@user_sync
def userfile_new( request, resume = False ):
    """ 
        new file 
    """
    fileform = UploadOtherFileForm( request.POST, request.FILES )
    if not fileform.is_valid():
        c = {
             'error_msg': fileform.errors['file']
            ,'user': request.user
            }
        return render_to_response('main/templates/error.html', c)


    profile = Profile.objects.get( user = request.user )

    if resume:
        url = '/'.join( [ ATS_URI, 'candidate/file/cv/' ] )
    else: 
        url = '/'.join( [ ATS_URI, 'candidate/file/new/' ] )

    #If the file is big enough to be readed by chunks
    params = {
               "candidate" : str( profile.atsid )
               ,"file" : request.FILES['file'] 
             }
    #y = mpopener.open(url, params)
    datagen, headers = multipart_encode( params )
    r = urllib2.Request( url, datagen, headers)
    y = urllib2.urlopen( r )
    #y = mpopener.open(url, params)

    #data = urllib.urlencode( {
    #         'candidate': profile.atsid 
    #        ,'file': request.FILES['file']
    #    } )
    #REQUEST TO ATS
    #r = urllib2.Request( url , data )
    #r = urllib2.Request( url )
    #y = urllib2.urlopen( r )
    read = y.read()
    y.close()
    ##END REQUEST
    #return HttpResponse( read )
    return user_files( request )

