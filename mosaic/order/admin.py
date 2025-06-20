from django.contrib import admin

# Register your models here.



from .models import Trader, Order

admin.site.register(Trader)
admin.site.register(Order)
