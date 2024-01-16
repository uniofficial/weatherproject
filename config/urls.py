"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from weatherApp.views import index, check_weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weatherApp/', include('weatherApp.urls', namespace='weatherApp')),
    path('', index, name='index'),  # index 함수를 불러옴
    path('check_weather/', check_weather, name='check_weather'),  # check_weather 함수를 불러옴
]
