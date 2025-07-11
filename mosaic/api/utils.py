import requests

def get_coordinates_from_address(address):
    """Get latitude and longitude from an address using Nominatim."""
    if not address:
        return None, None
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": address,
            "format": "json",
            "limit": 1
        }
        headers = {"User-Agent": "MosaicApp/1.0 (adedayhaftuu@example.com)"}
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
        print(f"No coordinates found for: {address}")
        return None, None
    except Exception as e:
        print(f"Geocoding failed for {address}: {str(e)}")
        return None, None



   