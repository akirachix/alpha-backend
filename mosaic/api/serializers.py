from rest_framework import serializers
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Payment
       fields = "__all__"

class STKPushSerializer(serializers.Serializer):
   phone_number = serializers.CharField()
   amount = serializers.DecimalField(max_digits=10, decimal_places=2)
   account_reference = serializers.CharField()
   transaction_desc = serializers.CharField()

from catalogue.models import Design
class DesignSerializer(serializers.ModelSerializer):
       class Meta:
              model=Design
              fields="__all__"







