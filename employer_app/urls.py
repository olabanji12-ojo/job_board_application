from django.urls import path
from .import views

urlpatterns = [
    path('', views.Employer_loginpage, name='Employer_loginpage'),
    path('Employer_homepage/', views.Employer_homepage, name='Employer_homepage'),
    path('job_creation', views.job_creation, name='job_creation'),
    path('jobs_created/<str:id>/', views.jobs_created, name='jobs_created'),
    path('job_details_employer/<str:id>/', views.job_details_employer, name='job_details_employer'),
    path('job_details_edit/<str:id>/', views.job_details_edit, name='job_details_edit'),
    path('view_applicants/<str:id>/', views.view_applicants, name='view_applicants'),
    path('applicants_profile/<str:id>/', views.applicants_profile, name='applicants_profile')
    
]
