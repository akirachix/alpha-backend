from django.db import models
from users.models import Users
from payment.models import Payment

# Create your models here.
class Transaction(models.Model):
     user = models.ForeignKey(Users,on_delete=models.CASCADE, null=True, blank=True)
     payment = models.ForeignKey(Payment, on_delete= models.CASCADE, null=True, blank=True)
     amount = models.DecimalField(max_digits = 10, decimal_places = 2)
     platform_fee = models.DecimalField(max_digits = 10, decimal_places = 2)
