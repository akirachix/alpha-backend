from django.db import models
from users.models import Users

USER_TYPE_CHOICES = [
    ('designer', 'Designer'),
    ('trader', 'Trader'),
 
]

class Order(models.Model):
    design_order = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='trader')
    order_date = models.DateField()
    delivery_method = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.design_order} by {self.user_type.full_name}"