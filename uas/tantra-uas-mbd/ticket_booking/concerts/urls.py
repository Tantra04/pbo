from django.urls import path
from . import views

urlpatterns = [
    path('', views.concerts_list, name='concerts_list'),
    path('book/<int:concerts_id>/', views.book_ticket, name='book_ticket'),
]