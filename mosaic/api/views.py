
# from rest_framework import viewsets
# from users.models import Users
# from django.shortcuts import render
# from order.models import Order


# from .serializers import UsersSerializer,OrderSerializer

# class UsersViewSet(viewsets.ModelViewSet):
#    queryset=Users.objects.all()
#    serializer_class=UsersSerializer
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset=Order.objects.all()
#     serializer_class= OrderSerializer




from rest_framework import viewsets
from users.models import Users
from order.models import Order
from .serializers import UsersSerializer, OrderSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer









  

