from django.contrib import admin
from .models import User, Profile, Job, Job_applicant

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Job_applicant)


# Register your models here.
