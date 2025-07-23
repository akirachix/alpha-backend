from rest_framework import serializers
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
from catalogue.models import Design,Category
class DesignSerializer(serializers.ModelSerializer):
       class Meta:
              model=Design
              fields="__all__"

from rest_framework import serializers
from users.models import Users  

class UsersSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'phone_number', 'address', 'latitude', 'longitude', 'user_type']  

from rest_framework import serializers
from shopping_cart.models import Shopping_cart, Item
class  ShoppingCartSerializer(serializers.ModelSerializer):
      class Meta:
             model=Shopping_cart
             fields="__all__"

class  ItemSerializer(serializers.ModelSerializer):
      class Meta:
             model=Item
             fields="__all__"


import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
import base64
import datetime
class DarajaAPI:
   def __init__(self):
       self.consumer_key = settings.DARAJA_CONSUMER_KEY
       self.consumer_secret = settings.DARAJA_CONSUMER_SECRET
       self.business_shortcode = settings.DARAJA_SHORTCODE
       self.passkey = settings.DARAJA_PASSKEY
       self.base_url = "https://sandbox.safaricom.co.ke"
       self.callback_url = settings.DARAJA_CALLBACK_URL
   def get_access_token(self):
       url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
       response = requests.get(url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
       return response.json()['access_token']
   def stk_push(self, phone_number, amount, account_reference, transaction_desc):
       access_token = self.get_access_token()
       timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
       password = base64.b64encode(f"{self.business_shortcode}{self.passkey}{timestamp}".encode()).decode()
       headers = {
           "Authorization": f"Bearer {access_token}",
           "Content-Type": "application/json"
       }
       payload = {
           "BusinessShortCode": self.business_shortcode,
           "Password": password,
           "Timestamp": timestamp,
           "TransactionType": "CustomerPayBillOnline",
           "Amount": int(amount),
           "PartyA": phone_number,
           "PartyB": self.business_shortcode,
           "PhoneNumber": phone_number,
           "CallBackURL": self.callback_url,
           "AccountReference": account_reference,
           "TransactionDesc": transaction_desc,
       }
       url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
       response = requests.post(url, headers=headers, json=payload)
       return response.json()

from rest_framework import serializers
from users.models import Users
from payment.models import Payment
from transaction.models import Transaction
from design_review.models import DesignReview
class PaymentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Payment
       fields = "__all__"
class STKPushSerializer(serializers.Serializer):
   phone_number = serializers.CharField()
   amount = serializers.DecimalField(max_digits=10, decimal_places=2)
   account_reference = serializers.CharField()
   transaction_desc = serializers.CharField()
from rest_framework import serializers
from order.models import Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'












