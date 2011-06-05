import urllib, urllib2
import simplejson

def create_profile(sender, instance, signal, created, **kwargs):
    """When user is created also create a matching profile."""
 
    from jobs.main.models import Profile
 
    if created:
        Profile( user = instance, email = instance.email ).save()


def edit_profile( sender, instance, signal, created, **kwargs ):
    """When profile is edited also create or update ATS candidate ."""

    profile = instance

    if not created and not instance.atsid: 
        r = urllib2.Request(
                 'http://localhost/ats/api/candidate/new/'
                ,data = urllib.urlencode( [
                     ( 'first_name', profile.first_name )
                    ,( 'last_name', profile.last_name )
                    ,( 'phone', profile.phone )
                    ,( 'mobile', profile.mobile )
                    ,( 'email_1', profile.email )
                 ] )
            )
        y = urllib2.urlopen( r )
        response = y.read()
        y.close()
    
        result = simplejson.loads( response )
        profile.atsid = result['candidate']
        profile.save()

    elif not created:
        r = urllib2.Request(
             'http://localhost/ats/api/candidate/%s/update/' % ( profile.atsid )
            ,data = urllib.urlencode( [
                ( 'first_name', profile.first_name )
               ,( 'last_name', profile.last_name )
               ,( 'phone',profile.phone )
               ,( 'mobile',profile.mobile )
               ,( 'email_1',profile.email )
            ] )
        )
        y = urllib2.urlopen( r )
        #response = y.read()
        #y.close()
    
        #result = simplejson.loads( response )
        
