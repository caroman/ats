import os
import urllib
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from ats.static.models import *
from ats.settings import MEDIA_ROOT, MEDIA_URL
################################################################################

FSS = FileSystemStorage( 
     location = MEDIA_ROOT
    ,base_url = MEDIA_URL
    )

################################################################################
class Candidate( models.Model ):
    #Automatic fields
    created_by = models.ForeignKey( User )
    updated_by = models.ForeignKey( User,
         related_name='%(class)s_related',
         null = True )
    created_time = models.DateTimeField(
        auto_now_add = True )
    updated_time = models.DateTimeField(
        auto_now = True )
    #Personal Information
    first_name = models.CharField(
        max_length = 100,
        help_text='First name' )
    last_name = models.CharField(
        max_length = 100,
        help_text='Last name' )
    phone = models.CharField(
         null = True
        ,blank = True
        ,max_length = 15
        ,help_text = 'With area code' )
    phone_extension = models.CharField(
         null = True
        ,blank = True
        ,max_length = 5
        ,help_text = 'Ext Number' )
    mobile = models.CharField(
         null = True
        ,blank = True
        ,max_length = 15
        ,help_text = 'With area code' )
    email_1 = models.EmailField(
         null = True
        ,blank = True )
    email_2 = models.EmailField(
         null = True
        ,blank = True )
    address = models.CharField(
         null = True
        ,blank = True
        ,max_length=100
        ,help_text='Number and Street' )
    city = models.CharField(
         null = True
        ,blank = True
        ,max_length=100
        ,help_text='City' )
    state = models.CharField(
         null = True
        ,blank = True
        ,max_length=100
        ,help_text='State' )
    postal_code = models.CharField(
         null = True
        ,blank = True
        ,max_length=100
        ,help_text='Postal code' )
    employer = models.CharField(
         null = True
        ,blank = True
        ,max_length = 100
        ,help_text='Current employer' )
     #Qualification
    professional_designations = models.ManyToManyField(
         ProfessionalDesignation
        ,null = True
        ,blank = True )
    managment_experience = models.ForeignKey( 
         ManagmentExperience
        ,null = True
        ,blank = True )
    work_locations = models.ManyToManyField( 
         WorkLocation
        ,null = True
        ,blank = True )
    salary = models.PositiveIntegerField(
         null = True
        ,blank = True
        ,help_text = 'Expected salary' )
    work_types = models.ManyToManyField( 
         WorkType
        ,null = True
        ,blank = True )
    keywords = models.CharField(
         null = True
        ,blank = True
        ,max_length = 100
        ,help_text='Keyword search' )
    resume = models.TextField(
         null = True
        ,blank = True )
 
    def __unicode__(self):
        return u"%s %s" % ( self.first_name,
                            self.last_name )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

#-------------------------------------------------------------------------------
class CandidateForm( ModelForm ):
    class Meta:
        model = Candidate
        exclude=('created_by',
                 'created_time',
                 'updated_time',
                 'updated_by')

#-------------------------------------------------------------------------------
class CandidatePersonalEditForm( ModelForm ):
    class Meta:
        model = Candidate
        fields = (
             'first_name'
            ,'last_name'
            ,'phone'
            ,'mobile'
            ,'email_1'
            ,'email_2'
            ,'city'
            ,'state'
            ,'postal_code'
            ,'address'
            )

#-------------------------------------------------------------------------------
class CandidateExperienceEditForm( ModelForm ):
    class Meta:
        model = Candidate
        fields = (
             'managment_experience'
            ,'salary'
            ,'professional_designations'
            ,'work_types'
            ,'work_locations'
            ,'keywords'
            )
    #called after is_valid
    #def clean_professional_designations( self ):
    #        data = self.cleaned_data['professional_designations']
    #        return '1'
            

#-------------------------------------------------------------------------------
def get_candidate_upload_to( instance, filename ):
    return os.path.join('candidate', str(instance.candidate.id), filename)

class CandidateFile( models.Model ):
    created_by = models.ForeignKey( User )
    created_time = models.DateTimeField(
        auto_now_add = True )
    candidate = models.ForeignKey( Candidate )
    title = models.CharField(
         max_length = 25
        ,help_text = 'Title' )
    file = models.FileField( 
         storage = FSS
        ,upload_to = get_candidate_upload_to )
    deleted = models.BooleanField(
        default = False )
    txt = models.TextField(
         null = True
        ,blank = True )
 
    def __unicode__( self ):
        return u"%s" % (self.title,)

    def download_link( self ):
        return u"/ats/main/%s" % ( urllib.pathname2url(self.file.url), )

    def download_name( self ):
        return u"%s" % ( os.path.basename( self.file.path ),)

    class Meta:
        ordering = ['title']
        verbose_name = 'Candidate File'
        verbose_name_plural = 'Candidate Files'


#-------------------------------------------------------------------------------
class CandidateFileForm( ModelForm ):
    class Meta:
        model = CandidateFile
        fields = (
             'candidate'
            #,'title'
            ,'file'
            )
 
################################################################################
class Mandate( models.Model ):
    #automatic fields
    created_by = models.ForeignKey( User )
    updated_by = models.ForeignKey( User,
         related_name='%(class)s_related',
         null = True )
    created_time = models.DateTimeField(
        auto_now_add = True )
    updated_time = models.DateTimeField(
        auto_now = True )
    #non automatic fields
    title = models.CharField(
        max_length = 100,
        help_text = 'Title of the mandate' )
    responsability = models.TextField(
         null = True
        ,blank = True )
    requirement = models.TextField(
         null = True
        ,blank = True )
    status = models.ForeignKey( MandateStatus
        ,null = True
        ,blank = True )
    posting_start_date = models.DateField(
         null = True
        ,blank = True )
    posting_end_date = models.DateField(
         null = True
        ,blank = True )
    hiring_manager = models.ForeignKey( HiringManager
        ,null = True
        ,blank = True
        ,help_text = 'Name of hiring manager' )
    posting_number = models.CharField(
         null = True
        ,blank = True
        ,max_length = 50
        ,help_text = 'Alpha numeric value' )
    confidential = models.BooleanField(
        null = False,
        default = False )
    city = models.CharField(
         null = True
        ,blank = True
        ,max_length = 50
        ,help_text = 'City' )
    candidate_source = models.CharField(
         null = True
        ,blank = True
        ,max_length = 50 )
    #closing information
    cost = models.PositiveIntegerField(
         null = True
        ,blank = True )
    consulting_time = models.DecimalField(
         null = True
        ,blank = True
        ,max_digits = 4
        ,decimal_places = 1
        ,help_text = 'Time in hours' )
    posting_sources = models.CharField(
         null = True
        ,blank = True
        ,max_length = 50 )
    comments = models.TextField(
         null = True
        ,blank = True )
    start_date = models.DateField(
         null = True
        ,blank = True
        ,help_text = 'Project start date' )
    end_date = models.DateField(
         null = True
        ,blank = True
        ,help_text = 'Project end date' )
    hired_number = models.PositiveIntegerField(
         null = True
        ,blank = True )

    def __unicode__(self):
        return u"%s" % (self.title,)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Mandate'
        verbose_name_plural = 'Mandates'


#-------------------------------------------------------------------------------
class MandateForm( ModelForm ):
    class Meta:
        model = Mandate
        exclude=(
             'created_by'
            ,'created_time'
            ,'updated_time'
            ,'updated_by')

#-------------------------------------------------------------------------------
class MandateEditForm( ModelForm ):
    class Meta:
        model = Mandate
        fields = (
             'title'
            ,'posting_start_date'
            ,'posting_end_date'
            ,'hiring_manager'
            ,'status'
            ,'city'
            ,'posting_number'
            )

#-------------------------------------------------------------------------------
class MandateResponsabilityForm( ModelForm ):
    class Meta:
        model = Mandate
        fields = ('responsability',)

#-------------------------------------------------------------------------------
class MandateRequirementForm( ModelForm ):
    class Meta:
        model = Mandate
        fields=('requirement', )


#-------------------------------------------------------------------------------
class MandateClosingForm( ModelForm ):
    class Meta:
        model = Mandate
        fields=(
             'candidate_source'
            ,'posting_sources'
            ,'start_date'
            ,'end_date'
            ,'consulting_time'
            ,'hired_number'
            ,'comments'
            )



################################################################################
class MAC( models.Model ):
    #automatic fields
    created_by = models.ForeignKey( User )
    updated_by = models.ForeignKey( User,
         related_name='%(class)s_related',
         null = True )
    created_time = models.DateTimeField( auto_now_add = True )
    updated_time = models.DateTimeField( auto_now = True )
    mandate = models.ForeignKey( Mandate
        ,null = True
        ,blank = True )
    candidate = models.ForeignKey( Candidate
        ,null = True
        ,blank = True )
    activity = models.ForeignKey( Activity
        ,null = True
        ,blank = True )
    status = models.ForeignKey( MACStatus
        ,null = True
        ,blank = True )
    #non automatic fields
    date = models.DateField(
         null = True
        ,blank = True )
    description = models.TextField(
         null = True
        ,blank = True )

    class Meta:
        ordering = ['-id']
        verbose_name = 'MAC'
        verbose_name_plural = 'MACs'

#-------------------------------------------------------------------------------
class MACNewForm(ModelForm):
    class Meta:
        model = MAC
        exclude=('created_by',
                 'created_time',
                 'updated_time',
                 'updated_by')

#-------------------------------------------------------------------------------
class MACUpdateForm( ModelForm ):
    class Meta:
        model = MAC
        fields = (
             'activity'
            ,'status'
            ,'date'
            ,'description'
            )

################################################################################





