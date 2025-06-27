from rest_framework import serializers

from shopping_cart.models import Shopping_cart
from users.models import Users


class  Shopping_cartSerializer(serializers.ModelSerializer):
       class Meta:
              model=Shopping_cart
              fields="__all__"
              
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'