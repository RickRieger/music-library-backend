from django.db import models

# Create your models here.


class Song(models.Model):
  title = models.CharField(max_length=255)
  artist = models.CharField(max_length=255)
  album = models.CharField(max_length=255)
  release_date = models.DateField()
  genre = models.CharField(max_length=255)
  like_count = models.IntegerField(default=0)
  dislike_count = models.IntegerField(default=0)
 
