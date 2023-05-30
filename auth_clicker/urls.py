from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_logout, name='login'),
    path('logout/', views.user_logout),
    path('registration/', views.user_registration, name='registration'),
    path('user/<int:pk>/', views.UserDetail.as_vivew()),
]
