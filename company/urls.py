from django.conf.urls import url
from . import views

app_name = 'company'

urlpatterns = [
	url(r'company/(?P<slug>[\w-]+)/$', views.company_detail, name='company_detail'),
]