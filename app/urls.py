from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.HomeView.as_view()),
    url(r'how-it-works/$', views.how_it_works, name='how_it_works'),
]
