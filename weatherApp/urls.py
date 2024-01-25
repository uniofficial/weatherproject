from django.urls import path
from . import views

app_name = 'weatherApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('check_weather/', views.check_weather, name='check_weather'),
]