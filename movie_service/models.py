from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'categories'
        
class Movie(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=4096)
    release_date = models.DateField(auto_now=True, null=True, blank=True)
    rating = models.IntegerField(default=None, null=True, blank=True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    duration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(240)], default=0)
    hasReservationsAvailable = models.IntegerField(default=None, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'movies'

class Cinema(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cinemas'

class Room(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    seats = models.PositiveIntegerField()
    cinema = models.ForeignKey(Cinema, related_name='rooms', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rooms'

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('expired', 'Expired'),
        ('confirmed', 'Confirmed')
    ]

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rank = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    seats = models.PositiveIntegerField()
    seance = models.ForeignKey('Seance', related_name='reservations', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    expiresAt = models.DateTimeField()

    def __str__(self):
        return str(self.uid)

    class Meta:
        db_table = 'reservations'

class Seance(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.UUIDField()
    date = models.DateTimeField()
    room = models.ForeignKey(Room, related_name='seances', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} - {self.date}"

    class Meta:
        db_table = 'seances'
