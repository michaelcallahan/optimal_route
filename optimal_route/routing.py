import requests

ORS_API_KEY = 'YOUR_KEY_HERE'

def calculate_route(start_coords, end_coords):
    url = 'https://api.openrouteservice.org/v2/directions/driving-car'
    params = {
        'api_key': ORS_API_KEY,
        'start': f"{start_coords[1]},{start_coords[0]}",
        'end': f"{end_coords[1]},{end_coords[0]}"
    }
    response = requests.get(url, params=params)
    data = response.json()
    route_coords = data['features'][0]['geometry']['coordinates']
    distance = data['features'][0]['properties']['segments'][0]['distance'] / 1000  # in kilometers
    return route_coords, distance
