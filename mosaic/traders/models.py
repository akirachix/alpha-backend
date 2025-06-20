from django.db import models

class Traders(models.Model):
    trader = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()
   