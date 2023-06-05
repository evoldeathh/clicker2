from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auther_clicker.urls')),
    path('', include('backend.urls')),
    path('', include('frontend.urls')),
]
