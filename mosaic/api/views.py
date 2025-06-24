from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from catalogue.models import Design
from designers.models import Designers
from design_review.models import design_review
from order.models import Order
from payment.models import Payment
from shopping_cart.models import Shopping_cart
from traders.models import Trader
from transaction.models import Transaction

from .serializers import (DesignSerializer,DesignersSerializer,TraderSerializer,OrderSerializer,PaymentSerializer,Shopping_cartSerializer,TransactionSerializer,design_reviewSerializer)


class DesignViewSet(viewsets.ModelViewSet):
    queryset=Design.objects.all()
    serializer_class=DesignSerializer
class DesignersViewSet(viewsets.ModelViewSet):
    queryset=Designers.objects.all()
    serializer_class=DesignersSerializer
class TraderViewSet(viewsets.ModelViewSet):
    queryset=Trader.objects.all()
    serializer_class= TraderSerializer
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class= OrderSerializer
class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class= PaymentSerializer
class Shopping_cartViewSet(viewsets.ModelViewSet):
    queryset=Shopping_cart.objects.all()
    serializer_class=Shopping_cartSerializer
class Transaction(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
class design_review(viewsets.ModelViewSet):
    queryset=design_review.objects.all()
    serializer_class=design_reviewSerializer



  

