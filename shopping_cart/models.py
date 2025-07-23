from django.db import models
from users.models import Users
from catalogue.models import Design

class Item(models.Model):
    design_item=models.ForeignKey(Design, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)
class Shopping_cart(models.Model):
    item=models.ManyToManyField(Item,related_name='cart')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
  



   


