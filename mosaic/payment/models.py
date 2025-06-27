from django.db import models
from order.models import Order
from user.models import User


# Create your models here.
class Payment(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    phone_number = models.CharField()
    mpesa_receipt_number = models.CharField()
    paid_at = models.DateField
   