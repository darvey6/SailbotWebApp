from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sailbot-home'),
    path('wind/', views.wind, name='sailbot-wind'),
    path('winchmotor/', views.winchmotor, name='sailbot-winchmotor'),
    path('ruddermotor/', views.ruddermotor, name='sailbot-ruddermotor'),
    path('gps/', views.gps, name='sailbot-gps'),
    path('boomangle/', views.boomangle, name='sailbot-boomangle'),
    path('bms/', views.bms, name='sailbot-bms'),
    path('accelerometer/', views.accelerometer, name='sailbot-accelerometer'),
]
