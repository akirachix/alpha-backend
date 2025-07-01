# from rest_framework import serializers
# from users.models import Users
# from order.models import Order


# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = '__all__'


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#          model = Order
#          fields = '__all__' 




from rest_framework import serializers
from users.models import Users
from order.models import Order

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'