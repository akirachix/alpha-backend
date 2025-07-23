from rest_framework import viewsets
from django.shortcuts import render
from .serializers import DesignSerializer
from .serializers import (
    TransactionSerializer, DesignReviewSerializer, ShoppingCartSerializer,
    UsersSerializer, PaymentSerializer, STKPushSerializer, OrderSerializer,ItemSerializer
)
from transaction.models import Transaction
from design_review.models import DesignReview
from shopping_cart.models import Shopping_cart, Item
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
from order.models import Order
class TransactionViewSet(viewsets.ModelViewSet):
   queryset = Transaction.objects.all()
   serializer_class = TransactionSerializer
  
class DesignReviewViewSet(viewsets.ModelViewSet):
   queryset=DesignReview.objects.all()
   serializer_class=DesignReviewSerializer
class ItemViewSet(viewsets.ModelViewSet):
   queryset=Item.objects.all()
   serializer_class=ItemSerializer
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
            checkout_request_id = response.get('CheckoutRequestID', None)
            user = None
            if checkout_request_id:
                payment = PaymentDetails.objects.create(
                    phone_number=data['phone_number'],
                    amount=data['amount'],
                    account_reference=data['account_reference'],
                    transaction_desc=data['transaction_desc'],
                    mpesa_checkout_id=checkout_request_id,
                    quantity= 1,
                    type = 'payment',
                    condition='New',
                    price=data['amount'],
                )
                if user:
                    if user.role == 'trader':
                        payment.trader = user
                    elif user.role == 'designer':
                        payment.upcycler = user
                    payment.save()
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

@api_view(['POST'])
def daraja_callback(request):
    callback_data = request.data
    print("Daraja Callback Data:", callback_data)
    try:
        stk_callback = callback_data['Body']['stkCallback']
        checkout_request_id = stk_callback['CheckoutRequestID']
        result_code = stk_callback['ResultCode']
        result_desc = stk_callback['ResultDesc']
        payment = PaymentDetails.objects.get(mpesa_checkout_id=checkout_request_id)
        payment.result_code = str(result_code)
        payment.result_description = result_desc
        if result_code == 0:
            items = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            item_dict = {item['Name']: item['Value'] for item in items}
            payment.mpesa_receipt_number = item_dict.get('MpesaReceiptNumber')
            trans_date_str = str(item_dict.get('TransactionDate'))
            trans_date = datetime.datetime.strptime(trans_date_str, '%Y%m%d%H%M%S')
            payment.transaction_date = timezone.make_aware(trans_date, timezone.get_current_timezone())
            payment.amount_from_callback = item_dict.get('Amount')
            payment.phone_number_from_callback = item_dict.get('PhoneNumber')
            payment.payment_status = 'Completed'
        else:
            payment.payment_status = 'Failed'
        payment.save()
    except PaymentDetails.DoesNotExist:
        print(f"Payment with CheckoutRequestID {checkout_request_id} not found.")
    except Exception as e:
        print(f"Error processing Daraja callback: {e}")
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})



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















