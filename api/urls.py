from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = 'api'

urlpatterns = [
    url(r'jobs/(?P<slug>\w+)$' ,views.Jobsviews.as_view(), name="api_jobs"),
    url(r'company/(?P<slug>\w+)$' ,views.Company_views.as_view(), name="api_comapny"),
    url(r'user/(?P<id>\w+)$' ,views.Users_views.as_view(), name="api_users"),
    ]