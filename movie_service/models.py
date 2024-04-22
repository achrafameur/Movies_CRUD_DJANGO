from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    release_date = models.DateField()
    rating = models.IntegerField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'movies'
