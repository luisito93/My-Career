from django.contrib import admin
from .models import Jobs, Company,Cv, UserProfile,Education, School, Office, Experience, Award

class JobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'office', 'salery','job_type','created')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city','since', 'contact_info')

class CvAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title','cv') 

class User_profileAdmin(admin.ModelAdmin):
    list_display = ('user','slug', 'city', 'country','gender','created')
    
class EducationAdmin(admin.ModelAdmin):
    list_display = ('education_level', 'degree','year')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'job_title','job_from','job_to')

class AwardAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'year')

admin.site.register(Jobs, JobsAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Cv ,CvAdmin)
admin.site.register(UserProfile, User_profileAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(School)
admin.site.register(Office)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Award, AwardAdmin)