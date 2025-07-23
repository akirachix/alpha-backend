from django.db import models
from order.models import Order
# Create your models here.
class DesignReview(models.Model):
  design_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='dr_design_reviews',null=True, blank=True)
  rating_value = models.IntegerField()
  comment = models.TextField()




class Order(models.Model):
   name = models.CharField(max_length=100)
   created_at = models.DateTimeField(auto_now_add=True)


   def __str__(self):
       return self.name

