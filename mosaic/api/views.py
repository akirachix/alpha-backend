from django.shortcuts import render
from rest_framework import viewsets
from catalogue.models import Design
from .serializers import DesignSerializer

class DesignViewSet(viewsets.ModelViewSet):
    queryset=Design.objects.all()
    serializer_class=DesignSerializer




  

