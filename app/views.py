from django.shortcuts import render
from django.views.generic import ListView
from jobs.models import Jobs
from django.conf import settings

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
        context['title'] = 'Find a Job | ' + settings.SITE_NAME
        return context

def how_it_works(request):
    context = {
        'title': 'How It Works | ' + settings.SITE_NAME
    }
    return render(request, 'others/how_it_works.html', context)
