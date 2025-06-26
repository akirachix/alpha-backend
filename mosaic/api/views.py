from rest_framework import viewsets
from django.shortcuts import render
from users.models import Users


from .serializers import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
   queryset=Users.objects.all()
   serializer_class=UsersSerializer









  

