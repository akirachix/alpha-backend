from django.db import models

# Create your models here.
class design_review(models.Model):
   design_order = models.ForeignKey(Order, on_delete= models.CASCADE)
   rating_value = models.IntegerField()
   comment = models.TextField()