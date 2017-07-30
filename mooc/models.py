from django.db import models

# Create your models here.
class Topic(models.Model):
    content = models.CharField(max_length=10000)    

