from django.db import models
from order.models import Order



# Create your models here.
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    amount = models.DecimalField()
    phone_number = models.CharField()
    mpesa_receipt_number = models.CharField()
    paid_at = models.DateField
    created_at = models.DateField
    update_at = models.DateField
    delivery_at = models.DateField()