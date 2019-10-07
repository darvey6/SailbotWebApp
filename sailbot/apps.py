from django.apps import AppConfig

class SailbotConfig(AppConfig):
    name = 'sailbot'
    verbose_name = "My Application"
    def ready(self):
        from threading import Thread
        from .network_table import index
        thread = Thread(target=index.subscribe)
        thread.start()
