from rest_framework import viewsets
from django.shortcuts import render
from users.models import Users
from .serializers import UsersSerializer
from .serializers import Shopping_cartSerializer
from shopping_cart.models import Shopping_cart


class UsersViewSet(viewsets.ModelViewSet):
   queryset=Users.objects.all()
   serializer_class=UsersSerializer


class Shopping_cartViewSet(viewsets.ModelViewSet):
    queryset=Shopping_cart.objects.all()
    serializer_class=Shopping_cartSerializer


