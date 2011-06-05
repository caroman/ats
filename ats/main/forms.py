from django.forms import ModelForm
from ats.main.models import *

#CANDIDATE######################################################################
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
            ,'phone_extension'
            ,'mobile'
            ,'email_1'
            ,'email_2'
            ,'city'
            ,'state'
            ,'postal_code'
            ,'address'
            ,'employer'
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
class CandidateFileForm( ModelForm ):
    class Meta:
        model = CandidateFile
        fields = (
             'candidate'
            #,'title'
            ,'file'
            )
 
#MANDATE########################################################################
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

#MAC############################################################################
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

