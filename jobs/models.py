from django.db import models
from django.db.models.signals import post_save
from froala_editor.fields import FroalaField
from djmoney.models.fields import MoneyField
from django.utils.crypto import get_random_string
from company.models import Office
from django.conf import settings
from datetime import date, timedelta

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title


class Jobs(models.Model):
    JOB_TYPES_CHOICES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Temporary', 'Temporary'),
        ('Intern', 'Intern'),
        ('Contractor', 'Contractor'),
        ('Other Type', 'Other Type')
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs_category')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='job_company')
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    description = FroalaField()
    job_type = models.CharField(
        max_length=100, choices=JOB_TYPES_CHOICES, default='Full Time')
    promotion_value = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    expire_time = models.DateTimeField(null=True, blank=True)
    applied_users = models.ManyToManyField(User, blank=True, related_name='applied_users')
    saved_users = models.ManyToManyField(User, blank=True, related_name='saved_users')
    tags = models.TextField(max_length=100, default="")

    def save(self, *args, **kwargs):
        self.slug = get_random_string(length=32)
        self.tags = self.tags.split(",")
        super(Jobs, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ApplicationInfo(models.Model):
    job = models.OneToOneField(Jobs, on_delete=models.CASCADE, related_name='application_info')
    experience = models.IntegerField(default=0)
    application_email = models.URLField(max_length=300, null=True, blank=True)
    application_url = models.URLField(max_length=300, null=True, blank=True)
    instruction = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.application_email


class CompensationInfo(models.Model):
    COMPENSATION_UNITS = (
        ('Hourly', 'Hourly'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
        ('One Time', 'One Time')

    )
    job = models.OneToOneField(Jobs, on_delete=models.CASCADE, related_name='compensation_info')
    amount = MoneyField(max_digits=14, null=True, blank=True, decimal_places=2, default_currency='USD')
    unit = models.CharField(max_length=100, choices=COMPENSATION_UNITS, default='Monthly')
    max_compensation = MoneyField(max_digits=14, null=True, blank=True, decimal_places=2, default_currency='USD')
    min_compensation = MoneyField(max_digits=14, null=True, blank=True, decimal_places=2, default_currency='USD')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.amount


class CustomAttribute(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, related_name='custom_attributes')
    attribute = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.key


def application_info_created_receiver(sender, instance, created, *args, **kwargs):
    if created:
        ApplicationInfo.objects.create(job=instance)


post_save.connect(application_info_created_receiver, sender=Jobs)


def compensation_info_created_receiver(sender, instance, created, *args, **kwargs):
    if created:
        CompensationInfo.objects.create(job=instance)


post_save.connect(compensation_info_created_receiver, sender=Jobs)
