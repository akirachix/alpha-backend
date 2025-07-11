from django.db import models
# from order.models import Order
from users.models import Users

class Payment(models.Model):
   
   
   amount = models.DecimalField(max_digits=10, decimal_places=2)
   phone_number = models.CharField(max_length=15)
   mpesa_receipt_number = models.CharField(max_length=100)
   

