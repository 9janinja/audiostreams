from django.db import models
from admin.song.models import Song
# Create your models here.


class Homepage(models.Model):

    name = models.CharField(max_length=150, default= None, blank=True)
    artist = models.CharField(max_length=150, default= None, blank=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default= None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
    	return self.name
