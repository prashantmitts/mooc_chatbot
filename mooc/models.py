from django.db import models

# Create your models here.


class Topic(models.Model):
    content = models.CharField(max_length=10000)
    title = models.CharField(max_length=40, default='Title')
    video = models.FileField(upload_to='videos/', default="video")
    
    def __str__(self):
        return self.title