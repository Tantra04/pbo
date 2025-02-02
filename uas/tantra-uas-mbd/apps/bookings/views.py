from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking, Event

def create_booking(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.save()
            return redirect('booking_detail', booking.pk)
    else:
        form = BookingForm()
    
    return render(request, 'bookings/booking_form.html', {'form': form, 'event': event})