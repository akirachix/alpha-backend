<<<<<<< HEAD
from django.shortcuts import render

from rest_framework import viewsets
from .models import Users
from .serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer
=======
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from api.serializers import UsersSerializer
from api.utils import get_coordinates_from_address

class UserCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        address = self.request.data.get('address')
        if address:
            lat, lon = get_coordinates_from_address(address)
            if lat is None or lon is None:
                print(f"Failed to geocode address: {address}")
                serializer.save(latitude=None, longitude=None)
            else:
                serializer.save(latitude=lat, longitude=lon)
        else:
            serializer.save(latitude=None, longitude=None)






>>>>>>> af3f64c53f9e112c757ad6cc5ba6edcbfb6c27e8
