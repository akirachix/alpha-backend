from django.db import models
from traders.models import Trader

# Create your models here.
class Shopping_cart(models.Model):
    trader = models.ForeignKey(Trader, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)