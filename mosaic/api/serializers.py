from rest_framework import serializers
from users.models import Users  

class UsersSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'latitude', 'longitude', 'user_type']  
