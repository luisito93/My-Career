from django.conf.urls import url
from . import views

app_name = 'jobs'

urlpatterns = [
	url(r'^jobs-$', views.jobs, name='jobs'),
    url(r'^jobs/(?P<slug>[\w-]+)/$', views.job_detail, name='job_detail'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^jobs/company/(?P<slug>[\w-]+)/$', views.job_at_company, name='job_at_company'),
]