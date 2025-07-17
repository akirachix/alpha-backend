from django.db import models
from users.models import Users
from catalogue.models import Design

class Shopping_cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


class Shopping_cart_item(models.Model):
    shopping_cart=models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)
    design_item=models.ForeignKey(Design, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    shopping_cart=models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
   


