from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('app.urls', namespace="app")),
    url(r'^logout/$', logout, name ='logout'),
    url(r'^api/',include('api.urls', namespace="api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
