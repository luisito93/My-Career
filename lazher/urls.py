from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from accounts import views as accounts_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('app.urls', namespace="app")),
    path('', include('company.urls', namespace="company")),
    path('', include('jobs.urls', namespace="jobs")),
    path('', include('userprofile.urls', namespace="userprofile")),
    url(r'^login/$', accounts_views.signin, name='login'),
    url(r'^password_change/$', login_required(accounts_views.password_change), name='password_change'),
    url(r'^register/$', accounts_views.signup, name='register'),
    url(r'^logout/$', logout, name ='logout'),
    url(r'^api/',include('api.urls', namespace="api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
