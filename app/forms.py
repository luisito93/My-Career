from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cv


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = True)
    zipcode = forms.IntegerField(required = False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'zipcode')

    def save(self,commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.zipcode = self.cleaned_data['zipcode']

        
        if commit:
            user.save()

        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')


class resume_upload(forms.ModelForm):
    cv = forms.FileField(required = True)
    job_title = forms.CharField(required = True)

    def save(self, commit=False):
        cvs = super(resume_upload, self).save(commit=False)
        cvs.cv = self.cleaned_data['cv']
        cvs.job_title = self.cleaned_data['job_title']
        
        if commit:
            cvs.save()

        return cvs

    class Meta:
        model = Cv
        fields = ('cv', 'job_title',)