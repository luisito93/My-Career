from django.shortcuts import render
from .models import Jobs
from company.models import Company
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from json import loads as json_loads
from django.core.paginator import Paginator

def jobs(request):
    query = request.GET.get('keywords')
    location = request.GET.get('location')
    order = request.GET.get('order_by')
    per_page = request.GET.get('per_page')
    page_num = request.GET.get('page',1)

    if query:
        results = Jobs.objects.filter(title__icontains=query)
        title = query + " Jobs" + " | " + settings.SITE_NAME
	    
        if location:
            results = Jobs.objects.filter(office__company__city__icontains=location)
            title = query + " Jobs " + "in " + location + " | " + settings.SITE_NAME
	        
    if location:
        title = "All jobs in " + location + " | " + settings.SITE_NAME
        results = Jobs.objects.filter(title__icontains=query, office__company__city__icontains=location)

    elif not query and not location:
        title = "Job results"
        results = Jobs.objects.all()

    if order:
        results = results.order_by(order)
    else:
        order = "-created"
        results = results.order_by("-created")

    if per_page:
        paginator = Paginator(results, per_page)
    else:
        per_page = 9
        paginator = Paginator(results, per_page)

    results = paginator.get_page(page_num)


    context = {
        'title': title,
        'items': results,
        'location': location,
        'query': query,
        'order':order,
        'per_page':per_page,
        'page_num':page_num,
    }
    
    return render(request, 'jobs.html', context)


def browse(request):
    company = Company.objects.all()
    title = 'Browse Jobs' + " | " + settings.SITE_NAME
    context = {
        'title':title,
        'company':company,
    }
    return render(request, 'browse.html', context)


def job_at_company(request, slug):
    company = Company.objects.get(slug=slug)
    results = Jobs.objects.filter(office__company__slug=slug)
    title = 'Jobs at ' + str(company) + " | " + settings.SITE_NAME
    context = {
        'title':title,
        'company':company,
        'items':results
    }

    return render(request, 'jobs.html',context)


def job_detail(request,slug):
    jobs = Jobs.objects.get(slug=slug)
    title = str(jobs) + " | " + settings.SITE_NAME
    context = {
        'title':title,
        'jobs':jobs,
    }
    return render(request, 'job_detail.html', context)

