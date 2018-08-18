from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils import timezone


class Album(models.Model):
    name = models.CharField(default="", max_length=30)
    weight = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    authur = models.CharField(default="", max_length=30)

    def __str__(self):
        return self.name

    def date_created_prettyfy(self):
        return self.date_created.strftime('%b %e %Y')


class Snap(models.Model):
    image = models.ImageField(upload_to='images/', default="")
    name = models.TextField(default="", max_length=20)
    pub_date = models.DateTimeField(default=timezone.now)
    caption = models.CharField(default=name, max_length=30)
    likes = models.PositiveSmallIntegerField(default=0)
    authur = models.CharField(default="", max_length=30)
    album = models.ManyToManyField('snaps.Album', related_name='album_snaps')
    tags = ArrayField(models.CharField(max_length=20, blank=True, default=""), default=[]) 

    def __str__(self):
        return self.caption
    
    def pub_date_prettyfy(self):
        return self.pub_date.strftime('%b %e %Y')

    def data(self):
        details = {
            'image': self.image,
            'title': self.name,
            'pub_date': self.pub_date,
            'caption': self.caption,
            'likes': self.likes,
            'album': self.album
        }
        return details
