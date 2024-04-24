from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'categories'
        
class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    release_date = models.DateField()
    rating = models.IntegerField(default=None, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'movies'
