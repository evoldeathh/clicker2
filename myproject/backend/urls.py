from django.urls import path
from . import views

boosts = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lonely_boost = views.BoostViewSet.as_view({
    'put': 'partial_update',
})

urlpatterns = [
    path('call_click/', views.call_click),
    path('boosts/', boosts, name='boosts'),
    path('boost/<int:pk>/', lonely_boost, name='boost')
]
