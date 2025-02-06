from django.db import models
from django.contrib.auth.models import User

class Concerts(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_tickets = models.IntegerField()
    tickets_sold = models.IntegerField(default=0)
    image = models.ImageField(upload_to='concert_images/', blank=True, null=True)
    
    def available_tickets(self):
        return self.total_tickets - self.tickets_sold

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concerts, on_delete=models.CASCADE)
    tickets_booked = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')  # Status pemesanan
    confirmation_code = models.CharField(max_length=20, blank=True, null=True)  # Kode konfirmasi unik

    def __str__(self):
        return f"Booking for {self.concert.name} by {self.user.username}"