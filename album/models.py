from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField()
    short_description = models.TextField()
    
    def __str__(self):
        return self.title