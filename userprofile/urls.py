from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'userprofile'

urlpatterns = [    
    url(r'^profile/$', login_required(views.profile), name='profile'),
    url(r'^resume/$', login_required(views.resume), name='resume'),
    url(r'^resume/(?P<slug>[\w-]+)/$', login_required(views.resume_view), name='resume_view'),
    url(r'^resumes/new/$', login_required(views.upload_resume), name='upload_resume'),

]
