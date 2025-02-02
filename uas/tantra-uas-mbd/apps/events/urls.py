from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ini akan menangani /
    path('list/', views.event_list, name='event_list'),  
    path('<int:pk>/', views.event_detail, name='event_detail'),
]
