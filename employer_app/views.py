from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from employee_app.forms import JobForm
from employee_app.models import User, Profile, Job, Job_applicant
from django.contrib.auth.decorators import login_required



def Employer_loginpage(request):
    if request.user.is_authenticated:
        return redirect('Employer_homepage')
    

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user:
            
            if user.role == 'employer':
                login(request, user)
                return redirect('Employer_homepage')
            
            else:
                return HttpResponse('invalid role')
            
        else:
            return HttpResponse('Email or Password is not correct')

    
    return render(request, 'employer/Employer_loginpage.html')

@login_required(login_url='Employer_loginpage')
def Employer_homepage(request):
    jobs = Job.objects.all()
    
    context = {'jobs':jobs}
    return render(request, 'employer/Employer_homepage.html', context)


def job_creation(request):
    # job = Job.objects.get(id=id)
    # user = User.objects.get(id=id)
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.jobs_created  = request.user
            forms.save()
            return redirect('Employer_homepage')
            
    context = {'form':form}
    return render(request, 'employer/job_creation.html', context)

def job_details_employer(request, id):
    # user = User.objects.get(id=id)
    job = Job.objects.get(id=id)
    
    context = {'job':job}
    return render(request, 'employer/job_details_employer.html', context)

def job_details_edit(request, id):
    job = Job.objects.get(id=id)
    # user = User.objects.get(id=id)
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_details', id=job.id)
    
    context = {'form':form, 'job': job}
    return render(request, 'employer/job_creation.html', context)


def jobs_created(request, id):
    
    user = User.objects.get(id=id)
    job_created = request.user.job_creators.all()
    
    
    context = {'job_created':job_created, 'user':user}
    return render(request, 'employer/jobs_created.html', context)

def view_applicants(request, id):
    # user = request.id
    job = Job.objects.get(id=id)  
    job_applicants = job.employee_applicant.all()  

    context = {'job': job, 'job_applicants': job_applicants}
    return render(request, 'employer/view_applicants.html', context)

def applicants_profile(request, id):
    user = User.objects.get(id=id)
    
    
    context = {'user':user}
    return render(request, 'employer/applicants_profile.html', context)


# Create your views here.
