from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    applicants = models.ForeignKey('Job', on_delete=models.CASCADE, null=True, blank=True, related_name='employee_applicant')
    
    ROLE_CHOICES = {
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    }
    
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'role']
    
    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=200, null=True, blank=True)
    CV = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(default='download.jpg', upload_to='static/images', null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.name}'
    
    
class Job(models.Model):
    employee_applied = models.ManyToManyField(User, blank=True, related_name='employee')
    jobs_created =models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='job_creators')
    job_name = models.CharField(max_length=200)
    description = models.TextField()
    company_name = models.CharField(max_length=100)
    tracking_id = models.IntegerField(null=True, blank=True)
    # job_applied = models.BooleanField(default=False)
    
    def __str__(self):
        return self.job_name
    
class Job_applicant(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'role': 'employee'})
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    id_number = models.IntegerField()
    
    def __str__(self):
        return f'{self.user} -- {self.job}'
    


# Create your models here.
