from rest_framework import serializers
from shopping_cart.models import Shopping_cart



class  ShoppingCartSerializer(serializers.ModelSerializer):
       class Meta:
              model=Shopping_cart
              fields="__all__"
              