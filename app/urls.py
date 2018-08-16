from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index),
    url(r'^jobs-$', views.jobs, name='jobs'),
    url(r'^jobs/(?P<slug>[\w-]+)/$', views.job_detail, name='job_detail'),
    url(r'^job/save_job/$', views.job_detail, name='save_job'),
    url(r'^jobs/company/(?P<slug>[\w-]+)/$', views.job_at_company, name='job_at_company'),
    url(r'^company/(?P<slug>[\w-]+)/$', views.company_detail, name='company_detail'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^register/$', views.signup, name='register'),
    url(r'^resumes/$', login_required(views.resumes), name='resumes'),
   url(r'^resume/(?P<slug>[\w-]+)/$', login_required(views.resume_view), name='resume_view'),
    url(r'^resumes/new/$', login_required(views.upload_resume), name='upload_resume'),
]
