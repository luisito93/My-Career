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
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^browse_jobs/$', views.browse_jobs, name='browse_jobs'),
    url(r'^jobs/company/(?P<slug>[\w-]+)/$', views.job_at_company, name='job_at_company'),
    url(r'^company/(?P<slug>[\w-]+)/$', views.company_detail, name='company_detail'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^password_change/$', login_required(views.password_change), name='password_change'),
    url(r'^profile/(?P<user>[\w-]+)/$', login_required(views.profile), name='profile'),
    url(r'^register/$', views.signup, name='register'),
    url(r'^resumes/$', login_required(views.resumes), name='resumes'),
    url(r'^resume/(?P<slug>[\w-]+)/$', login_required(views.resume_view), name='resume_view'),
    url(r'^resumes/new/$', login_required(views.upload_resume), name='upload_resume'),
    # others pages url
    url(r'how-it-works/$', views.how_it_works, name='how_it_works'),
]
