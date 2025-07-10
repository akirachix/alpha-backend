from django.db import models
from order.models import Order

class design_review(models.Model):
   design_order = models.ForeignKey(Order, on_delete= models.CASCADE)
   rating_value = models.IntegerField()
   comment = models.TextField()
