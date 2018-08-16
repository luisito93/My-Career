from django.contrib import admin
from .models import Jobs, Company,Cv

class JobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salery','job_type','created')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'contact_info')

class CvAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title','cv') 


admin.site.register(Jobs, JobsAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Cv ,CvAdmin)