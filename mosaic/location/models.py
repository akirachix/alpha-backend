from django.db import models

# Create your models here.
address = models.CharField(max_length=512, blank=True, null=True)

from users.models import Users  
class Location(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='locations')
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=512, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"{self.user.full_name} - {self.address or 'No address'}"