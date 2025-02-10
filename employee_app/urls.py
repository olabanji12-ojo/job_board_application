from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.welcome_page, name='welcome_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('home_page/', views.home_page, name='home_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('applicant_job_details/<str:id>/', views.applicant_job_details, name='applicant_job_details'),
    path('job_details_confirm/<str:id>/', views.job_details_confirm, name='job_details_confirm'),
    path('job_unapply_confirm/<str:id>/', views.job_unapply_confirm, name='job_unapply_confirm'),
    path('jobs_applied/<str:id>/', views.jobs_applied, name='jobs_applied'),
    path('profiles_page/', views.profiles_page, name='profiles_page'),
    path('profile_id_page/<str:id>/', views.profile_id_page, name='profile_id_page'),
    
    path('profile_edit_page/<str:id>/', views.profile_edit_page, name='profile_edit_page'),
    
    path('myaccount/<str:id>/', views.myaccount, name='myaccount'),
    
]
