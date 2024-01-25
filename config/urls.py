from django.contrib import admin
from django.urls import path, include
from weatherApp.views import index, check_weather
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weatherApp/', include('weatherApp.urls', namespace='weatherApp')),
    path('', index, name='index'),  # index 함수를 불러옴
    path('check_weather/', check_weather, name='check_weather'),  # check_weather 함수를 불러옴
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)