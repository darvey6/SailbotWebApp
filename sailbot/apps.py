from django.apps import AppConfig
from threading import Thread
from network_table import index

if __name__ == "__main__":
    thread = Thread(target=index.subscribe)
    thread.start()
