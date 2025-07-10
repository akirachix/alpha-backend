from django.shortcuts import render
from rest_framework import viewsets
from payment.models import Payment 
from .serializers import PaymentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .daraja import DarajaAPI
from .serializers import STKPushSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response




class PaymentViewSet(viewsets.ModelViewSet):
   queryset=Payment.objects.all()
   serializer_class=PaymentSerializer

class OrderViewSet(viewsets.ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer


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




@api_view(['POST'])
def daraja_callback(request):
   print("Daraja Callback Data:", request.data)
   return Response({"ResultCode": 0, "ResultDesc": "Accepted"})


  

