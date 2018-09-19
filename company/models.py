from django.db import models
from django_countries.fields import CountryField
from froala_editor.fields import FroalaField
from django.utils.crypto import get_random_string
import datetime
from app.validators import validate_file_extension, image_path, face_detiction


YEAR_CHOICES = []
for r in range(1800, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))


def current_year():
    return datetime.date.today().year


class Company(models.Model):
    title = models.CharField(max_length=100, blank=False)
    display_name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(blank=True, default='')
    city = models.CharField(max_length=100, blank=False)
    country = CountryField(default='')
    Description = FroalaField()
    hiring_agency = models.BooleanField(default=False)
    eeo_text = models.TextField(null=True, blank=True)  # Equal Employment Opportunity legal disclaimer text
    since = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
    contact_info = models.CharField(max_length=100, blank=False, default="")
    website = models.URLField(max_length=100, blank=False, default="")
    facebook = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    logo = models.ImageField(upload_to=image_path, default=0, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = get_random_string(length=16)
        self.website = self.website.replace("https://", "")
        self.twitter = self.twitter.replace("https://", "")
        if self.display_name is None:
            self.display_name = self.title
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Office(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    country = CountryField(default='')
    city = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.company.title
