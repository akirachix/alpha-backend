from django.db import models

# Create your models here.
class Shopping_cart(models.Model):
    trader = models.ForeignKey(trader_details, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField()