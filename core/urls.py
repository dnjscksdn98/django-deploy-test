from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index/', include('tester.urls', namespace='index')),
    path('admin/', admin.site.urls),
]
