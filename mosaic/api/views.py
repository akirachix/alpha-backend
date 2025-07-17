from rest_framework import viewsets
from django.shortcuts import render
from .serializers import DesignSerializer
from .serializers import (TransactionSerializer,DesignReviewSerializer,ShoppingCartSerializer,UsersSerializer,PaymentSerializer, STKPushSerializer,OrderSerializer)
from transaction.models import Transaction
from design_review.models import DesignReview
from shopping_cart.models import Shopping_cart
from users.models import Users
from payment.models import Payment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .daraja import DarajaAPI
from rest_framework.decorators import api_view
from rest_framework.response import Response
from catalogue.models import Design
from api.utils import get_coordinates_from_address 
import requests
from catalogue.models import Design
from order.models import Order
class TransactionViewSet(viewsets.ModelViewSet):
   queryset = Transaction.objects.all()
   serializer_class = TransactionSerializer
  
class DesignReviewViewSet(viewsets.ModelViewSet):
   queryset=DesignReview.objects.all()
   serializer_class=DesignReviewSerializer
class ShoppingCartViewSet(viewsets.ModelViewSet):
   queryset=Shopping_cart.objects.all()
   serializer_class=ShoppingCartSerializer
class DesignViewSet(viewsets.ModelViewSet):
    queryset=Design.objects.all()
    serializer_class=DesignSerializer
def get_coordinates_from_address(address):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': address,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params, headers={'User-Agent': 'mosaic-app'})
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data['lat']), float(data['lon'])
    return None, None

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        address = self.request.data.get('address')
        lat, lon = None, None
        if address:
            lat, lon = get_coordinates_from_address(address)
        serializer.save(latitude=lat, longitude=lon)

    def perform_update(self, serializer):
        address = self.request.data.get('address')
        lat, lon = None, None
        if address:
            lat, lon = get_coordinates_from_address(address)
        serializer.save(latitude=lat, longitude=lon)

# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
   queryset = Transaction.objects.all()
   serializer_class = TransactionSerializer
class DesignReviewViewSet(viewsets.ModelViewSet):
   queryset=DesignReview.objects.all()
   serializer_class=DesignReviewSerializer

class PaymentViewSet(viewsets.ModelViewSet):
   queryset=Payment.objects.all()
   serializer_class=PaymentSerializer
class STKPushView(APIView):
   def post(self, request):
       serializer = STKPushSerializer(data=request.data)
       if serializer.is_valid():
           data = serializer.validated_data
           daraja = DarajaAPI()
           response = daraja.stk_push(
               phone_number=data['phone_number'],
               amount=data['amount'],
               account_reference=data['account_reference'],
               transaction_desc=data['transaction_desc']
           )
           return Response(response)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
@api_view(['POST'])
def daraja_callback(request):
   print("Daraja Callback Data:", request.data)
   return Response({"ResultCode": 0, "ResultDesc": "Accepted"})

class ShoppingCartViewSet(viewsets.ModelViewSet):
   queryset=Shopping_cart.objects.all()
   serializer_class=ShoppingCartSerializer

from order.models import Order
from .serializers import OrderSerializer
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
















# from rest_framework import viewsets
# from users.models import Users
# from .serializers import UsersSerializer
# from api.utils import get_coordinates_from_address
# import requests
# from django.shortcuts import render
# from rest_framework import viewsets
# from payment.models import Payment
# from .serializers import PaymentSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .daraja import DarajaAPI
# from .serializers import STKPushSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
class PaymentViewSet(viewsets.ModelViewSet):
   queryset=Payment.objects.all()
   serializer_class=PaymentSerializer
class STKPushView(APIView):
   def post(self, request):
       serializer = STKPushSerializer(data=request.data)
       if serializer.is_valid():
           data = serializer.validated_data
           daraja = DarajaAPI()
           response = daraja.stk_push(
               phone_number=data['phone_number'],
               amount=data['amount'],
               account_reference=data['account_reference'],
               transaction_desc=data['transaction_desc']
           )
           return Response(response)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from catalogue.models import Design
from .serializers import DesignSerializer
class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
@api_view(['POST'])
def daraja_callback(request):
   print("Daraja Callback Data:", request.data)
   return Response({"ResultCode": 0, "ResultDesc": "Accepted"})

class ShoppingCartViewSet(viewsets.ModelViewSet):
   queryset=Shopping_cart.objects.all()
   serializer_class=ShoppingCartSerializer


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer















