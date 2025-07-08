from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
def get_address_from_coords(latitude, longitude):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse((latitude, longitude), exactly_one=True, timeout=10)
        return location.address if location else "Unknown location"
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        return "Geocoding failed"