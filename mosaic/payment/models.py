from django.db import models
from order.models import Order
from users.models import Users


class Payment(models.Model):
   order = models.ForeignKey(Order, on_delete=models.CASCADE)
   users = models.ForeignKey(Users, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits = 10, decimal_places = 2)
  phone_number = models.CharField()
  mpesa_receipt_number = models.CharField()
  paid_at = models.DateField
