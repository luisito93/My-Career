from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import MyRegistrationForm, resume_upload
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Jobs, Company, Cv

def index(request):
    context = {
        'title':'Find a Job | OdamaCareer',
    }
    
    if request.method == 'GET':
        response = HttpResponse("cookie")
        response.set_cookie('hhh',"khra")
        value = request.COOKIES.get('hhh')
        print(value)
          
    return render(request,"index.html",context)
    
def jobs(request):
	query = request.GET.get('keywords')
	location = request.GET.get('location')
	
	if query:
	    results = Jobs.objects.filter(title__icontains=query)
	    title = query + " Jobs"
	    
	    if location:
	        results = Jobs.objects.filter(company__city__icontains=location)
	        title = query + " Jobs " + "in " + location
	        
	if location:
	    title = "All jobs in " + location
	    results = Jobs.objects.filter(title__icontains=query, company__city__icontains=location)
	
	context = {
	    'title':title,
	    'items': results,
		'location': location,
        'query': query,
    }

	return render(request, 'jobs.html', context)


def job_at_company(request, slug):
    company= Company.objects.get(slug=slug)
    results = Jobs.objects.filter(company__slug=slug)
    context = {
        'company':company,
	    'items':results
	}

    return render(request, 'jobs.html',context)

def job_detail(request,slug):
	jobs = Jobs.objects.get(slug=slug)
	context = {
		'jobs':jobs,
	}
	return render(request, 'job_detail.html', context)

def company_detail(request,slug):
	company = Company.objects.get(slug=slug)
	jobs = Jobs.objects.filter(company__slug=slug)
	context = {
		'company':company,
		'jobs':jobs,
	}
	return render(request, 'company_detail.html', context)


def signin(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                if next:
                    return redirect(next)
                else:
                    return redirect("/")
        else:
            messages.error(request,"Oops! That didn't work. Please check your username and password and try again")
    else:
            form = AuthenticationForm(request.POST)
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'accounts/signin.html',{'form': form,'next':next,})


def signup(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			next = request.GET.get("next")
			if next:
			    return redirect(next)
			else:
			    return redirect('/')

	else:
		form = MyRegistrationForm()
        		
	if request.user.is_authenticated:
		return redirect('/')
	else:
		return render(request, 'accounts/signup.html',{'form': form, 'title':'Sign Up',})

def resumes(request):
	user = request.user
	resumes = Cv.objects.filter(user=user)

	context = {
	    'title':'Resumes',
		'resumes':resumes,
	}
	return render(request, 'resumes.html', context)

def resume_view(request, slug):
	resumes = Cv.objects.filter(slug=slug)

	context = {
		'title':'Resumes',
		'resumes':resumes,
	}
	return render(request, 'resumes.html', context)

def upload_resume(request):
	if request.method == 'POST':
		form = resume_upload(request.POST, request.FILES)
		if form.is_valid():
			cv_form = form.save()
			cv_form.user = request.user
			form.save(commit=True)
			return redirect('/resumes')
		else:
			messages.error(request,"Oops! That didn't work. Please try again")
	else:
		form = resume_upload()

	return render(request, 'upload_resume.html',{'form':form, 'title':'Upload a Resume'})