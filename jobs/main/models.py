from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User

from jobs.main.signals import create_profile, edit_profile


signals.post_save.connect( create_profile, sender=User )

class Profile( models.Model ):
    user = models.ForeignKey( User, unique=True )
    first_name = models.CharField(
        max_length = 100)
    last_name = models.CharField(
        max_length = 100)
    phone = models.CharField(
         null = True
        ,blank = True
        ,max_length = 15
        ,help_text = 'With area code' )
    mobile = models.CharField(
         null = True
        ,blank = True
        ,max_length = 15
        ,help_text = 'With area code' )
    email = models.EmailField(
         null = True
        ,blank = True )
    atsid = models.IntegerField(
         default = 0 )

    def get_absolute_url(self):
        return ( 'profiles_profile_detail'
                ,()
                ,{ 'username': self.user.username })
    get_absolute_url = models.permalink( get_absolute_url )

    def is_sync(self):
        if self.atsid:
            return True
        else:
            return False
 
