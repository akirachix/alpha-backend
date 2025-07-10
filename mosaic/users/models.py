from django.db import models

USER_TYPE_CHOICES = [
       ('Designer', 'Designer'),
       ('Trader', 'Trader'),
]

class Users(models.Model):
   full_name = models.CharField(max_length=255)
   email = models.EmailField(unique=True)
   phone_number = models.CharField(max_length=20)
   password = models.CharField(max_length=128)
   latitude = models.FloatField()
   longitude = models.FloatField()
   address = models.CharField(max_length=512, blank=True, null=True)
   user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Designer')


def __str__(self):
       return f"{self.full_name} ({self.get_type_display()})"


