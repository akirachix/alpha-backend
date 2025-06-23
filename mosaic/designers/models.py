from django.db import models

# Create your models here.

class Designers(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128) 
    latitude = models.FloatField()
    longitude = models.FloatField()

  
