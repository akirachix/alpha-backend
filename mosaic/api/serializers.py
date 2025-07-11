from rest_framework import serializers
<<<<<<< HEAD
from users.models import Users  

class UsersSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'latitude', 'longitude', 'user_type']  
=======
from catalogue.models import Design
class DesignSerializer(serializers.ModelSerializer):
       class Meta:
              model=Design
              fields="__all__"







>>>>>>> f716beba9e48da903ad17573b6fdc841dc4e42ad
