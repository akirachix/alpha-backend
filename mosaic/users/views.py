from django.shortcuts import render

from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer