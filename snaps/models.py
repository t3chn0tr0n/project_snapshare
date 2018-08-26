from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Album(models.Model):
    name = models.CharField(default="", max_length=30, null=True)
    weight = models.PositiveIntegerField(default=0, null=True)
    likes = models.PositiveIntegerField(default=0, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    author = models.CharField(default="", max_length=30, null=True)

    def date_created_prettyfy(self):
        return self.date_created.strftime('%b %e %Y')


class Snap(models.Model):
    image = models.ImageField(upload_to='images/', default="images/404.jpg", null=True)
    name = models.TextField(default="", max_length=20, null=True)
    pub_date = models.DateTimeField(default=timezone.now, null=True)
    caption = models.CharField(default=name, max_length=30, null=True)
    likes = models.PositiveSmallIntegerField(default=0, null=True)
    author = models.CharField(default="", max_length=30, null=True)
    album = models.ManyToManyField('snaps.Album', related_name='album_snaps')
    tags = ArrayField(models.CharField(max_length=20, blank=True, default=""), default=[], null=True) 
    
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
