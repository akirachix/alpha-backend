from django.db import models

# Create your models here.
class Trader(models.Model):
    trader = models.AutoField(primary_key=True)  
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.full_name

class Order(models.Model):
    design_order = models.AutoField(primary_key=True)
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    order_date = models.DateField()
    delivery_method = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.design_order} by {self.trader.full_name}"