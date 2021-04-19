from django.apps import AppConfig


class WardenappConfig(AppConfig):
    name = 'Wardenapp'

    def ready(self):
        import Wardenapp.signals
