from django.urls import path
from backend import views as bv
from auther_clicker import views

urlpatterns = [
    path('call_click/', bv.call_click),
]
