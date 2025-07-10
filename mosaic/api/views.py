from rest_framework import viewsets
from users.models import Users
from api.serializers import UsersSerializer
from api.utils import get_coordinates_from_address

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
    

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        address = self.request.data.get('address')
        if address:
            lat, lon = get_coordinates_from_address(address)
            serializer.save(latitude=lat, longitude=lon)
        else:
            serializer.save(latitude=None, longitude=None)

    def perform_update(self, serializer):
        address = self.request.data.get('address')
        if address:
            lat, lon = get_coordinates_from_address(address)
            serializer.save(latitude=lat, longitude=lon)
        else:
            serializer.save()
