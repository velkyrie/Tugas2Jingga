from django.db import models

# Create your models here.
class MyWatchlist(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.CharField(max_length=255)
    review = models.TextField()