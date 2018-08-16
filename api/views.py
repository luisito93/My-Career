from app.models import Jobs,Company
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import JobsSerializer,CompanySerializer, UserSerializer

class Jobsviews(generics.ListCreateAPIView):
    serializer_class = JobsSerializer
    http_method_names = ['get']
    def get_queryset(self):
        slug = self.kwargs['slug']
        query = Jobs.objects.filter(slug=slug)
        return query
        
class Company_views(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    http_method_names = ['get']
    def get_queryset(self):
        slug = self.kwargs['slug']
        query = Company.objects.filter(slug=slug)
        return query
        
        
class Users_views(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get']
    def get_queryset(self):
        id = self.kwargs['id']
        query = User.objects.filter(id=id)
        return query