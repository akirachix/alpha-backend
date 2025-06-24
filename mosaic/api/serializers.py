from rest_framework import serializers
from catalogue.models import Design
from designers.models import Designers
from design_review.models import design_review
from order.models import Order
from payment.models import Payment
from shopping_cart.models import Shopping_cart
from traders.models import Trader
from transaction.models import Transaction


class DesignSerializer(serializers.ModelSerializer):
       class Meta:
              model=Design
              fields="__all__"
class DesignersSerializer(serializers.ModelSerializer):
       class Meta:
              model=Designers
              fields="__all__"
class TraderSerializer(serializers.ModelSerializer):
       class Meta:
              model=Trader
              fields="__all__"
class OrderSerializer(serializers.ModelSerializer):
       class Meta:
              model=Order
              fields="__all__"
class PaymentSerializer(serializers.ModelSerializer):
       class Meta:
              model=Payment
              fields="__all__"
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
