from django.db import models
from traders.models import Trader
from payment.models import Payment

# Create your models here.
class Transaction(models.Model):
 trader = models.ForeignKey(Trader, on_delete= models.CASCADE)
 payment = models.ForeignKey(Payment, on_delete= models.CASCADE)
 amount = models.DecimalField(max_digits = 10, decimal_places = 2)
 platform_fee = models.DecimalField(max_digits = 10, decimal_places = 2)