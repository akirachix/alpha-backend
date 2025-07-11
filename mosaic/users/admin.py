from django.contrib import admin
from .models import Users



admin.site.register(Users)


class UsersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'address', 'latitude', 'longitude', 'user_type']

