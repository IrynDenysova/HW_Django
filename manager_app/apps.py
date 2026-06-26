from django.apps import AppConfig


class ManagerAppConfig(AppConfig):
    name = 'manager_app'


    def ready(self):
        import manager_app.signals
