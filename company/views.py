from django.shortcuts import render
from company.models import Company
from jobs.models import Jobs
from django.conf import settings

def company_detail(request, slug):
    company = Company.objects.get(slug=slug)
    jobs = Jobs.objects.filter(office__company__slug=slug)

    context = {
        'title': str(company) + ' | ' + settings.SITE_NAME,
        'company': company,
        'jobs': jobs,
    }
    return render(request, 'company_detail.html', context)
