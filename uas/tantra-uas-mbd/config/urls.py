from django.contrib import admin
from django.urls import path, include
from apps.events import views  # Import views from events app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # URL for the home page
    path('events/', include('apps.events.urls')),
    path('bookings/', include('apps.bookings.urls')),
    path('users/', include('apps.users.urls')),
]
