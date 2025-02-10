from django.apps import AppConfig


class EmployeeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employee_app'
    
    def ready(self):
        import employee_app.signals
    

