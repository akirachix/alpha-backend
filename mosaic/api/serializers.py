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
>>>>>>> df0fd973e8168909e79b74a49ccc5e5df48df02a
from catalogue.models import Design
class DesignSerializer(serializers.ModelSerializer):
       class Meta:
              model=Design
              fields="__all__"

<<<<<<< HEAD







=======
from rest_framework import serializers
from users.models import Users  

class UsersSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'latitude', 'longitude', 'user_type']  
>>>>>>> df0fd973e8168909e79b74a49ccc5e5df48df02a
