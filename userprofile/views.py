from django.shortcuts import render
from django.conf import settings
from userprofile.models import Education, Experience, Cv, Award
from django.contrib.auth import get_user_model
from .forms import resume_upload

User = get_user_model()


def profile(request):
    user = request.user
    profile = User.objects.get(userprofile__user=user)
    education = Education.objects.filter(user=user).order_by('-year_to')
    cv = Cv.objects.get(user__userprofile__user=user)
    experience = Experience.objects.filter(user=user).order_by("-job_to")
    awards = Award.objects.filter(user=user).order_by("-year")
    
    context = {
        'title':'My Profile' + ' | ' +settings.SITE_NAME,
        'profile':profile,
        'education':education,
        'cv':cv,
        'experience':experience,
        'awards':awards,
    }
    return render(request, 'profile.html',context)


def resume(request):
    user = request.user
    profile = User.objects.get(userprofile__user=user)
    education = Education.objects.filter(user=user).order_by('-year_to')
    experience = Experience.objects.filter(user=user).order_by("-job_to")
    awards = Award.objects.filter(user=user).order_by("-year")

    context = {
        'title':'My Resume' + ' | ' +settings.SITE_NAME,
        'education':education,
        'experience':experience,
        'awards':awards,
    }
    return render(request, 'resume.html', context)

def upload_resume(request):
    if request.method == 'POST':
        form = resume_upload(request.POST, request.FILES)
        if form.is_valid():
            cv_form = form.save()
            cv_form.user = request.user
            form.save(commit=True)
            return redirect('/resumes')
        else:
            messages.error(request, "Oops! That didn't work. Please try again")
    else:
        form = resume_upload()
    context = {
        'form': form, 
        'title': 'Upload a Resume' + ' | ' + settings.SITE_NAME
    }
    return render(request, 'upload_resume.html',context)

