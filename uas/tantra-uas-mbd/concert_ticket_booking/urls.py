# concert_ticket_booking/urls.py

from django.contrib import admin
from django.urls import path, include
from apps.events.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Halaman utama menuju view home
    path('events/', include('apps.events.urls')),  # Menyertakan URL dari apps.events
]
