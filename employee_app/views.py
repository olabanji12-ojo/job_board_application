from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import RegisterCreationForm, ProfileForm
from .models import User, Profile, Job
from django.contrib.auth.decorators import login_required





def welcome_page(request):
    if request.user.is_authenticated:
        return redirect('login_page')
    
    context = {}
    return render(request, 'base/welcome_page.html', context)

@login_required(login_url='login_page')
def home_page(request):
    if request.user.role == 'employer':
        return redirect('Employer_homepage')
    
    jobs = Job.objects.all()
    
    
    context = {'jobs': jobs}
    return render(request, 'base/home_page.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user:
            
            if user.role == 'employee':
                login(request, user)
                return redirect('home_page')
            else:
                return HttpResponse('Invalid role')
            
        else:
            return HttpResponse('Email or Password is not correct')
 

    context = {}
    return render(request, 'base/login_page.html', context)


def logout_page(request):
    
    logout(request)
    
    return redirect('login_page')
    
    
def register_page(request):
    form = RegisterCreationForm
    
    if request.method == 'POST':
        form = RegisterCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.name  = user.name.lower()
            user.email  = user.email.lower()
            user.save()
            
            login(request, user)
            if user.role == 'employee':
                return redirect('home_page')
            
            elif user.role == 'employer':
                return redirect('Employer_homepage')
            
            else:
                return HttpResponse('You didn\'t select a role')
        else:
            return HttpResponse('An error has occured during registration')

            
    context = {'form': form}
    return render(request, 'base/register_page.html', context)
    
    
    
def applicant_job_details(request, id):
    job = Job.objects.get(id=id)
    applied =  request.user.employee.filter(job_name=job).exists()
    print(applied)
    
    
    context = {'job':job, 'applied':applied}
    return render(request, 'base/applicant_job_details.html', context)


def job_details_confirm(request, id):
    # user = User.objects.get(id=id)
    job = Job.objects.get(id=id)
    if request.method == 'POST':
        job.employee_applied.add(request.user)
        request.user.applicants = job
        request.user.save()
        job.save()
        return redirect('home_page')
       
    context = {'job':job}
    return render(request, 'base/job_details_confirm.html', context)

def job_unapply_confirm(request, id):
    job = Job.objects.get(id=id)
    if request.method == 'POST':
        job.employee_applied.remove(request.user)
        return redirect('home_page')
    
    context = {'job':job}
    return render(request, 'base/job_unapply_confirm.html', context)
    
def jobs_applied(request, id):
    # job = Job.objects.get(id=id)
    user = User.objects.get(id=id)
    jobs_applied = request.user.employee.all()
    
    
    context = {'jobs_applied': jobs_applied, 'user':user}
    return render(request, 'base/jobs_applied.html', context)


def profiles_page(request):
    users = User.objects.all()
    # profiles = Profile.objects.all()
    context = {'users':users}
    return render(request, 'base/profiles_page.html', context)

 
def profile_id_page(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    # form =
    
    context = {'profile':profile}
    return render(request, 'base/profile_id_page.html', context)

def profile_edit_page(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    # profile.user.name == request.user.name
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile )
        if form.is_valid():
            initial = form.save(commit=False)
            initial.user.name = request.user
            initial.save()
            return redirect('profile_id_page', id=user.id)

    
    context = {'form':form}
    return render(request, 'base/profile_edit_page.html', context)


def myaccount(request, id):
    user = User.objects.get(id=id)
    
    context = {'user': user}
    return render(request, 'base/myaccount.html', context)


    
    




# Create your views here.
