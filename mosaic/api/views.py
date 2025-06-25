from django.shortcuts import render

from rest_framework import viewsets
from traders.models import Trader
from .serializers import TraderSerializer
class TraderViewSet(viewsets.ModelViewSet):
    queryset=Trader.objects.all()
    serializer_class=TraderSerializer
