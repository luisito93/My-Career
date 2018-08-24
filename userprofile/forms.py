from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Cv


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