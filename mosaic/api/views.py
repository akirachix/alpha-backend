from rest_framework import viewsets
from django.shortcuts import render
from .serializers import Shopping_cartSerializer
from shopping_cart.models import Shopping_cart


class Shopping_cartViewSet(viewsets.ModelViewSet):
    queryset=Shopping_cart.objects.all()
    serializer_class=Shopping_cartSerializer








