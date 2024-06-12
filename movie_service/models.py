from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'categories'
        
class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=255)
    release_date = models.DateField(auto_now=True, null=True, blank=True)
    rating = models.IntegerField(default=None, null=True, blank=True)
    rate = models.IntegerField(default=None, null=True, blank=True)
    duration = models.IntegerField(default=None, null=True, blank=True)
    hasReservationsAvailable = models.IntegerField(default=None, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'movies'
