from app.models import Jobs, Company
from rest_framework import serializers
from django.contrib.auth.models import User


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = ('title','country','Description', 'city','contact_info','website','facebook','twitter','linkedin','logo')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
        
     
class JobsSerializer(serializers.HyperlinkedModelSerializer):
    applyed_users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    company = CompanySerializer()
    class Meta:
        model = Jobs
        fields = ('title','company','job_type','salery','applyed_users','tags',)
        