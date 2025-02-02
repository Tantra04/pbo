from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:event_id>/', views.create_booking, name='create_booking'),
]