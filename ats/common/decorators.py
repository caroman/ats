from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

##############################################################################
login_needed = user_passes_test( lambda u: not u.is_anonymous()
                                ,login_url = '/ats/login/' )

##############################################################################
def group_required(group):
    """
    This is similar to the above decorator 'logged_in_or_basicauth'
    except that it requires the logged in user to be in a specific
    group.

    Use:

    @group_required('group')
    def your_view:
        ...

    """
    def in_group( user, group ):
        if user:
            return user.groups.filter(name=group).count() == 1
        return False

    def view_decorator(func):
        def wrapper(request, *args, **kwargs):
            if in_group( request.user, group ): 
                return func(request, *args, **kwargs)
            else:
                response = HttpResponse()
                response.status_code = 401
                return response
        return wrapper
    return view_decorator

