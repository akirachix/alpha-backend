from django.db import models
from users.models import Users
from catalogue.models import Design


class Shopping_cart(models.Model):
    # user = models.ForeignKey(Users, on_delete= models.CASCADE)
    # design=models.ForeignKey(Design, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    


