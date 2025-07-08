from django.urls import path
from .views import UserLocation
urlpatterns = [
    path('user/', UserLocation.as_view(), name='get-location'),
]




