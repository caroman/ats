from django import template
from django.template.defaultfilters import stringfilter
import os


register = template.Library()


@register.filter(name='basename')
@stringfilter
def basename(value):
    """
    in your template just after the {% extends .. %} tags 
    insert the {% load mytags %} tag.
    use your new filter to get filenames from a full file path:
    {{ render.media_file|basename }}
    """
    return os.path.basename(value)

