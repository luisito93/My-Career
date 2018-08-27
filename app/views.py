from django.shortcuts import render
from jobs.models import Jobs

def index(request):
    jobs = Jobs.objects.all().order_by("-created")
    context = {
        'title': 'Find a Job | OdamaCareer',
        'jobs':jobs,
    }

    return render(request,"index.html",context)


def how_it_works(request):
    return render(request, 'others/how_it_works.html')