
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import Shopping_cartSerializer,TransactionSerializer,design_reviewSerializer
from .models import Shopping_cart, Transaction, Design_review

# Create your views here.
class Shopping_cartViewSet(viewsets.ModelViewSet):
    queryset=Shopping_cart.objects.all()
    serializer_class=Shopping_cartSerializer
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
class Design_reviewViewSet(viewsets.ModelViewSet):
    queryset=Design_review.objects.all()
    serializer_class=design_reviewSerializer