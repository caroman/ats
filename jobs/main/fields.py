from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class ContentTypeRestrictedFileField( FileField ):
    """
    http://nemesisdesign.net/blog/coding/\
        django-filefield-content-type-size-validation/
    Same as FileField, but you can specify:
        * content_types
            list containing allowed content_types.
            Example: ['application/pdf', 'image/jpeg',
            'application/pdf', 'application/zip', 
            'application/vnd.ms-powerpoint', 'application/vnd.ms-excel', 
            'application/msword', 'application/vnd.oasis.opendocument.text', 
            'application/vnd.oasis.opendocument.spreadsheet', 
            'application/vnd.oasis.opendocument.presentation']
        * max_upload_size 
            a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):        
        data = super(ContentTypeRestrictedFileField, self).clean( *args
                                                                 ,**kwargs )
        
        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types or self.content_types is None:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('Filetype not supported.'))
        except AttributeError:
            pass        
            
        return data


   
