from rest_framework import viewsets
from django.shortcuts import render
from users.models import Users


from .serializers import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
   queryset=Users.objects.all()
   serializer_class=UsersSerializer

def get_coordinates_from_address(address):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'address': address,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params, headers={'User-Agent': 'mosaic-app'})
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data['lat']), float(data['lon'])
    return None, None
    

