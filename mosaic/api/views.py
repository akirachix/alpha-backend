
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import TransactionSerializer,DesignReviewSerializer
from transaction.models import Transaction
from design_review.models import DesignReview
# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
   queryset = Transaction.objects.all()
   serializer_class = TransactionSerializer
  
class DesignReviewViewSet(viewsets.ModelViewSet):
   queryset=DesignReview.objects.all()
   serializer_class=DesignReviewSerializer

from django.shortcuts import render
from rest_framework import viewsets
from catalogue.models import Design
from .serializers import DesignSerializer
class DesignViewSet(viewets.ModelViewSet):
    queryset=Design.objects.all()
    serializer_class=DesignSerializer






  

