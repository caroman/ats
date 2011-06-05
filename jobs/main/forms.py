from django import forms
from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField

from jobs.main.models import *
from jobs.main.fields import ContentTypeRestrictedFileField
 
class ProfileForm( ModelForm ):
 
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        try:
            #self.fields['email'].initial = self.instance.user.email
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
        except User.DoesNotExist:
            pass
 
    #email = forms.EmailField(label="Primary email",help_text='')
    captcha = CaptchaField()
 
    class Meta:
        model = Profile
        exclude = ('user','atsid','email')        
 
    def save(self, *args, **kwargs):
        """
        Update the primary email address on the related User object as well.
        """
        u = self.instance.user
        #u.email = self.cleaned_data['email']
        u.first_name = self.cleaned_data['first_name']
        u.last_name = self.cleaned_data['last_name']
        u.save()
        profile = super(ProfileForm, self).save(*args,**kwargs)
        return profile


class UploadCVFileForm( forms.Form ):
    file = forms.FileField()

    def clean_file(self):
        content_types = ['application/pdf', 'application/msword']
        max_upload_size = 2621440
        data = self.cleaned_data['file']
        content_type = data.content_type
        if content_types is None or content_type in content_types:
            if data.size <= max_upload_size:
                    return data
            else:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(max_upload_size), filesizeformat(data._size)))
        else:
            raise forms.ValidationError(_('Filetype not supported.'))

class UploadOtherFileForm( forms.Form ):
    file = forms.FileField()

    def clean_file(self):
        content_types = None
        max_upload_size = 2621440
        data = self.cleaned_data['file']
        content_type = data.content_type
        if content_types is None or content_type in content_types:
            if data.size <= max_upload_size:
                    return data
            else:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(max_upload_size), filesizeformat(data._size)))
        else:
            raise forms.ValidationError(_('Filetype not supported.'))
        


