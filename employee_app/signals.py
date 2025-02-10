from .models import User, Profile
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  user = instance
  if created and user.role == 'employee':
      Profile.objects.create(user=user)
      print('Profile Created')
      subject = 'Welcome to Emmanuel\'s website'
      message = 'we are glad you could make it'
      
      send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
)
  elif created and user.role == 'employer':
     Profile.objects.create(user=user)
     print('Profile Created') 
     subject = 'Welcome to Emmanuel\'s website'
     message = 'we are glad you could make it'
      
     send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
)
