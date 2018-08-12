from django.db import models
from django.contrib.auth.models import User


class Snap(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.TextField(default="", max_length=20)
    pub_date = models.DateTimeField()
    caption = models.CharField(default=name, max_length=20)
    likes = models.PositiveSmallIntegerField(default=0)
    album = models.CharField(default="General upload", max_length=20)

    def __str__(self):
        return self.caption
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
