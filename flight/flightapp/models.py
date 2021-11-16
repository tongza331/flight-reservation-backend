from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

SEAT_CLASS = (
    ('economy', 'Economy'),
    ('first', 'First')
)

TICKET_STATUS =(
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('CANCELLED', 'Cancelled')
)

GENDER = (
    ('male','MALE'),    #(actual_value, human_readable_value)
    ('female','FEMALE')
)

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.id}: {self.username}"

class Location(models.Model):
    city = models.CharField(max_length=64)
    city_thai = models.CharField(max_length=300)
    airport = models.CharField(max_length=64)
    airport_thai = models.CharField(max_length=300)
    code = models.CharField(max_length=3)
    country = models.CharField(max_length=64) # Only Thailand
    class Meta:
        db_table = "location"

    def __str__(self):
        return f"{self.city}:{self.code}"

class Ticket(models.Model):
    fid = models.CharField(max_length=10,primary_key=True)
    fnumber = models.CharField(max_length=50)
    origin = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="arrivals")
    depart_time = models.TimeField(null=True, blank=True)
    depart_date = models.DateField(null=True, blank=True)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    airline = models.CharField(max_length=64)
    fare = models.FloatField(null=True)
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS)
    class Meta:
        db_table = "ticket"

    def __str__(self):
        return f"{self.fid}: {self.origin} to {self.destination}, {self.seat_class}"

class Passenger(models.Model):
    username = models.CharField(max_length=64, blank=True,null=True)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, blank=True)
    #passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flights")
    #flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="passengers")
    class Meta:
        db_table = "passenger"
    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}, {self.gender}"

class Schedule(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bookings", blank=True, null=True)
    ref_no = models.CharField(max_length=6, unique=True)
    passenger = models.ManyToManyField(Passenger, related_name="flight_tickets")
    flight = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="tickets", blank=True, null=True)
    flight_departdate = models.DateField(blank=True, null=True)
    flight_returndate = models.DateField(blank=True, null=True)
    flight_fare = models.FloatField(blank=True,null=True)
    total_fare = models.FloatField(blank=True, null=True)
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS)
    booking_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=45, choices=TICKET_STATUS)
    class Meta:
        db_table = "schedule"

    def __str__(self):
        return self.ref_no
