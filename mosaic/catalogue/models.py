from django.db import models
from django.core.validators import MinValueValidator
class Category(models.Model):
    name=models.CharField(max_length=28,blank=True)
class Design(models.Model):
    design_id = models.CharField(primary_key=True, max_length=50)
    design_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material_type = models.CharField(max_length=50)
    design_image = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    design_size = models.CharField(max_length=20)
    category=models.ForeignKey(Category,null=True,on_delete=models.PROTECT)