from django.db import models

class Snap(models.Model):
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    caption = models.CharField(max_length=20)
    likes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.caption
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
