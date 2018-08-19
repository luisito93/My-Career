import os
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from PIL import Image
import numpy as np
import cv2
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
        filename = '{}.{}'.format(random_string, ext)
    return os.path.join(upload_to, filename)

def face_detiction(image):
    im = Image.open(image)
    face_cascade = cv2.CascadeClassifier('C:/Users/agoun/Desktop/haarcascade_frontalface_default.xml')
    image = np.array(im)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) < 1:
        raise ValidationError(u'Please upload a picture of your face')
    if len(faces) > 1:
        raise ValidationError(u'Your Picture have more than 1 face,Please upload a picture of your face')