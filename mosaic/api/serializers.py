from rest_framework import serializers

from shopping_cart.models import Shopping_cart




class  Shopping_cartSerializer(serializers.ModelSerializer):
       class Meta:
              model=Shopping_cart
              fields="__all__"
              
class  TransactionSerializer(serializers.ModelSerializer):
       class Meta:
              model=Transaction
              fields="__all__"

class  design_reviewSerializer(serializers.ModelSerializer):
       class Meta:
              model=design_review
              fields="__all__"

class TraderSerializer(serializers.ModelSerializer):
       class Meta:
              model=Trader
              fields="__all__"

