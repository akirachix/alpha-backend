from django.db import models

class Designers(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)  # Consider using Django's auth system for passwords
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.full_name