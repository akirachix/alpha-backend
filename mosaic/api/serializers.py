from rest_framework import serializers

from payment.models import Payment

from transaction.models import Transaction
from design_review.models import DesignReview
class  TransactionSerializer(serializers.ModelSerializer):
      class Meta:
             model=Transaction
             fields="__all__"
class  DesignReviewSerializer(serializers.ModelSerializer):
      class Meta:
             model=DesignReview
             fields="__all__"
from catalogue.models import Design




class PaymentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Payment
       fields = "__all__"

class STKPushSerializer(serializers.Serializer):
   phone_number = serializers.CharField()
   amount = serializers.DecimalField(max_digits=10, decimal_places=2)
   account_reference = serializers.CharField()
   transaction_desc = serializers.CharField()
class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = "__all__"



from rest_framework import serializers
from users.models import Users  

class UsersSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)






    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'latitude', 'longitude', 'user_type']  

