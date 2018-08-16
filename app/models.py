from django.db import models
import datetime
from django.contrib.auth.models import BaseUserManager
from django.utils.text import slugify
from django.contrib.auth.models import User
from .validators import validate_file_extension, image_path
from django.utils.crypto import get_random_string
from sorl.thumbnail import ImageField, get_thumbnail
from froala_editor.fields import FroalaField
from djmoney.models.fields import MoneyField

class Company(models.Model):
	title = models.CharField(max_length=100, blank=False)
	slug = models.SlugField(blank=True, default='')
	city = models.CharField(max_length=100, blank=False)
	contact_info = models.CharField(max_length=100, blank=False, default="")
	website = models.CharField(max_length=100,blank=False,default="")
	facebook = models.CharField(max_length=100, blank=True)
	twitter = models.CharField(max_length=100, blank=True)
	linkedin = models.CharField(max_length=100, blank=True)
	logo = models.ImageField(upload_to=image_path, default=0)

	def save(self, *args, **kwargs):
		self.slug = get_random_string(length=16)
		self.website = self.website.replace("https://", "")
		self.twitter = self.twitter.replace("https://", "")
		
		super(Company, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class Jobs(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(blank=True, default='')
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
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
		self.tags = self.tags.split(" ")
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