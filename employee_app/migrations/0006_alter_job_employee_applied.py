# Generated by Django 5.1.1 on 2025-02-03 15:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0005_job_tracking_id_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employee_applied',
            field=models.ManyToManyField(blank=True, null=True, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
    ]
