from django.db import models

# Create your models here.


class Payment(models.Model):
    design_order =  models.ForeignKey(Order, on_delete=models.CASCADE)
    trader =  models.ForeignKey(Trader, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places =2, max_digits =6)
    phone_number = models.CharField(max_length=20)
    mpesa_receipt_number = models.CharField(max_length=20)
    paid_at = models.DateField
    created_at = models.DateField
    update_at = models.DateField
    delivery_at = models.DateField

