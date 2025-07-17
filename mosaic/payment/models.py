from django.db import models

from users.models import Users



class Payment(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    phone_number = models.CharField(max_length=16)
    mpesa_receipt_number = models.CharField(max_length=100)


   
  
   
