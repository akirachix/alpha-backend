from rest_framework import viewsets
from django.shortcuts import render
from .serializers import ShoppingCartSerializer
from shopping_cart.models import Shopping_cart


class ShoppingCartViewSet(viewsets.ModelViewSet):
   queryset=Shopping_cart.objects.all()
   serializer_class=ShoppingCartSerializer