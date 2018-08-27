from django.contrib import admin
from jobs.models import Jobs, Category, ApplicationInfo, CompensationInfo, CustomAttribute
# Register your models here.


class JobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'office', 'salary','job_type','created')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


class ApplicationInfoAdmin(admin.ModelAdmin):
    list_display = ['application_email', 'experience']


class CompensationInfoAdmin(admin.ModelAdmin):
    list_display = ['amount', 'unit']


class CustomAttributeAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'value']


admin.site.register(Jobs, JobsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ApplicationInfo, ApplicationInfoAdmin)
admin.site.register(CompensationInfo, CompensationInfoAdmin)
admin.site.register(CustomAttribute, CustomAttributeAdmin)
