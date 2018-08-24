from django.db import models
from froala_editor.fields import FroalaField
from djmoney.models.fields import MoneyField
from django.utils.crypto import get_random_string
from company.models import Office
from django.conf import settings
import datetime


User = settings.AUTH_USER_MODEL

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

		