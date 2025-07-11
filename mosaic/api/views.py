<<<<<<< HEAD
=======
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
>>>>>>> df0fd973e8168909e79b74a49ccc5e5df48df02a

from rest_framework import viewsets
from users.models import Users
from .serializers import UsersSerializer
from api.utils import get_coordinates_from_address 
import requests
from django.shortcuts import render
from rest_framework import viewsets
from catalogue.models import Design
from .serializers import DesignSerializer
class DesignViewSet(viewets.ModelViewSet):
    queryset=Design.objects.all()
    serializer_class=DesignSerializer



def get_coordinates_from_address(address):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': address,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params, headers={'User-Agent': 'mosaic-app'})
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data['lat']), float(data['lon'])
    return None, None

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        address = self.request.data.get('address')
        lat, lon = None, None
        if address:
            lat, lon = get_coordinates_from_address(address)
        serializer.save(latitude=lat, longitude=lon)

    def perform_update(self, serializer):
        address = self.request.data.get('address')
        lat, lon = None, None
        if address:
            lat, lon = get_coordinates_from_address(address)
        serializer.save(latitude=lat, longitude=lon)


<<<<<<< HEAD

from django.shortcuts import render
from rest_framework import viewsets
from catalogue.models import Design
from .serializers import DesignSerializer
class DesignViewSet(viewsets.ModelViewSet):
    queryset=Design.objects.all()
    serializer_class=DesignSerializer






  

=======
>>>>>>> df0fd973e8168909e79b74a49ccc5e5df48df02a

