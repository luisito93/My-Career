import os
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.doc', '.docx', '.pdf', '.rtf', '.txt', '.odt', '.wps']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
        
def image_path(image, filename):
    upload_to = 'logo'
    ext = filename.split('.')[-1]
    random_string = get_random_string(length=32)
    if image.pk:
        filename = '{}.{}'.format(random_string, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(random_string, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
    