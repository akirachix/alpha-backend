from django.contrib import admin

# Register your models here.
from .models import Design
admin.site.register(Design)
from .models import Category
admin.site.register(Category)
