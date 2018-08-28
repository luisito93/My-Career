from django.shortcuts import render
from django.views.generic import ListView
from jobs.models import Jobs


class HomeView(ListView):
    model = Jobs
    template_name = 'index.html'
    context_object_name = 'jobs'
    paginate_by = 5

    def get_queryset(self):
        queryset = Jobs.objects.all().order_by("-created")
        return queryset

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Find a Job | OdamaCareer'
        return context


def index(request):
    jobs = Jobs.objects.all().order_by("-created")
    context = {
        'title': 'Find a Job | OdamaCareer',
        'jobs': jobs,
    }

    return render(request, "index.html", context)


def how_it_works(request):
    return render(request, 'others/how_it_works.html')
