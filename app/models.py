from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth.models import BaseUserManager
from django.utils.text import slugify
# from django.contrib.auth.models import User
from .validators import validate_file_extension,image_path, face_detiction
from django.utils.crypto import get_random_string
from sorl.thumbnail import ImageField, get_thumbnail
from froala_editor.fields import FroalaField
from djmoney.models.fields import MoneyField
from django.db.models.signals import post_save
from django_countries.fields import CountryField

User = settings.AUTH_USER_MODEL


YEAR_CHOICES = []
for r in range(1800, (datetime.datetime.now().year+1)):
	YEAR_CHOICES.append((r,r))


def current_year():
	return datetime.date.today().year


class Company(models.Model):
	title = models.CharField(max_length=100, blank=False)
	slug = models.SlugField(blank=True, default='')
	city = models.CharField(max_length=100, blank=False)
	country = CountryField(default='')
	Description = FroalaField()
	since = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
	contact_info = models.CharField(max_length=100, blank=False, default="")
	website = models.URLField(max_length=100,blank=False,default="")
	facebook = models.URLField(max_length=100, blank=True)
	twitter = models.URLField(max_length=100, blank=True)
	linkedin = models.URLField(max_length=100, blank=True)
	logo = models.ImageField(upload_to=image_path, default=0)

	def save(self, *args, **kwargs):
		self.slug = get_random_string(length=16)
		self.website = self.website.replace("https://", "")
		self.twitter = self.twitter.replace("https://", "")
		super(Company, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class Office(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	country = CountryField(default='')
	city = models.CharField(max_length=100, blank=False)
	
	def __str__(self):
		return self.company.title

class Jobs(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(blank=True, default='')
	office = models.ForeignKey(Office, on_delete=models.CASCADE)
	salery = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
	Description = FroalaField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	job_type = models.CharField(max_length=100, choices=(('Full Time', 'Full Time'),('Part Time', 'Part Time')),default='Full Time')
	applyed_users = models.ManyToManyField(User)
	saved_users = models.ManyToManyField(User, related_name='saved_users')
	tags = models.TextField(max_length=100,default="")
	    
		
	def save(self, *args, **kwargs):
		self.slug = get_random_string(length=32)
		self.tags = self.tags.split(",")
		super(Jobs, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

		
class Cv(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cv = models.FileField(upload_to='cvs', default='', validators=[validate_file_extension])
	slug = models.SlugField(blank=True,default='')
	job_title = models.CharField(max_length=100, default='')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		self.slug = get_random_string(length=32)
		super(Cv, self).save(*args, **kwargs)

	
	def __str__(self):
		return self.job_title

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	slug = models.SlugField(blank=True, default='')
	avatar = models.ImageField(validators=[face_detiction], upload_to='profile_images',default='/default.jpg', blank=False)
	country = CountryField(default='', blank=False)
	city = models.CharField(max_length=100, default='', blank=False)
	industry = models.CharField(max_length=100, default='', blank=False)
	gender = models.CharField(max_length=100, choices=(('Male', 'Male'),('Female', 'Female')),default='Male')
	about = models.TextField(max_length=255, default='',blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		self.slug = get_random_string(length=32)
		super(UserProfile, self).save(*args, **kwargs)

	def __str__(self):
		return self.user.email

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        cv = Cv.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)

class School(models.Model):
	name = models.CharField(max_length=100, default='', blank='False')
	def __str__(self):
		return self.name
		
class Education(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	education_level = models.CharField(max_length=100, choices=(('University', 'University'),('High School', 'High School')),default='University')
	degree = models.CharField(max_length=100,blank=False)
	education_description = models.TextField(max_length=255, default='',blank=False)
	year_from = models.IntegerField(choices=YEAR_CHOICES, default=current_year, blank=False)
	year_to = models.IntegerField(choices=YEAR_CHOICES, default=current_year, blank=False)


class Experience(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	job_title = models.CharField(max_length=100,blank=False)
	experience_description = models.TextField(max_length=255, default='',blank=False)
	job_from = models.IntegerField(choices=YEAR_CHOICES, default=current_year, blank=False)
	job_to = models.IntegerField(choices=YEAR_CHOICES, default=current_year, blank=False)
	
	def __str__(self):
		return self.user.email


class Award(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	award_description = models.TextField(max_length=255, default='',blank=False)
	year = models.IntegerField(choices=YEAR_CHOICES, default=current_year, blank=False)
	
	def __str__(self):
		return self.user.username
		return self.user.email

