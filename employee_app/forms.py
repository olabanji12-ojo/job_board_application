from django import forms
from .models import User, Profile, Job
from django.contrib.auth.forms import UserCreationForm

class RegisterCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'role', 'password1', 'password2']
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['skills', 'CV', 'profile_picture']
        
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_name', 'description', 'company_name', 'tracking_id']
        
        
    


