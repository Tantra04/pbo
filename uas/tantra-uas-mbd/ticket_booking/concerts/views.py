from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Concerts, Booking
from .forms import BookingForm
from django.db.models import Q 

def register(request):  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat! Silakan login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def concerts_list(request):
    concerts = Concerts.objects.all()
    return render(request, 'concerts/concerts_list.html', {'concerts': concerts})

@login_required
def book_ticket(request, concerts_id):
    concert = get_object_or_404(Concerts, id=concerts_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            tickets_requested = form.cleaned_data['tickets_booked']
            if tickets_requested > concert.available_tickets():
                messages.error(request, "Not enough tickets available!")
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.concert = concert
                booking.save()
                concert.tickets_sold += tickets_requested
                concert.save()
                messages.success(request, "Tickets booked successfully!")
                return redirect('booking_status') 
    else:
        form = BookingForm()
    return render(request, 'concerts/book_ticket.html', {'form': form, 'concert': concert})

@login_required
def booking_status(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'concerts/booking_status.html', {'bookings': bookings})

@login_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.status == 'pending':
        booking.status = 'confirmed'
        booking.confirmation_code = 'CONF-' + str(booking.id) 
        booking.save()
        messages.success(request, f"Booking {booking.id} telah dikonfirmasi.")
    else:
        messages.info(request, f"Booking {booking.id} sudah dikonfirmasi atau dibatalkan.")
    return redirect('booking_status')

@login_required
def search(request):
    query = request.GET.get('q')
    results = Concerts.objects.filter(
        Q(name__icontains=query) | 
        Q(date__icontains=query) | 
        Q(location__icontains=query)
    )
    return render(request, 'concerts/search_results.html', {'results': results, 'query': query})