from django.db import models
from company.models import Company
from django_countries.fields import CountryField
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
import datetime
from djmoney.models.fields import MoneyField
from django.conf import settings
from app.validators import validate_file_extension
User = settings.AUTH_USER_MODEL

YEAR_CHOICES = []
for r in range(1800, (datetime.datetime.now().year+1)):
	YEAR_CHOICES.append((r,r))


def current_year():
	return datetime.date.today().year

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
	salary_from = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
	salary_to = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

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

