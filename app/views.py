from django.shortcuts import render

def index(request):
    context = {
        'title': 'Find a Job | OdamaCareer',
    }

    return render(request,"index.html",context)


def how_it_works(request):
    return render(request, 'others/how_it_works.html')