from django.shortcuts import render, get_object_or_404
from .models import Event
from apps.bookings.forms import BookingForm 
from django.shortcuts import render  # Jika Anda menggunakan formulir ini di sini

def home(request):
    return render(request, 'events/index.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = BookingForm()  # Inisialisasi formulir
    return render(request, 'events/event_detail.html', {'event': event, 'form': form})

# ... (tampilan lain untuk bookings dan users)