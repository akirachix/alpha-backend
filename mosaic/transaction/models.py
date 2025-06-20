from django.db import models

# Create your models here.
class Transaction(models.Model):
 trader = models.ForeignKey(trader_details, on_delete= models.CASCADE)
 payment = models.ForeignKey(payment, on_delete= models.CASCADE)
 amount = models.DecimalField()
 platform_fee = models.DecimalField()





