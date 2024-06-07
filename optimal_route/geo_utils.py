from geopy.geocoders import Nominatim, Photon

def get_city_coordinates(city, country):
    geolocator = Photon(user_agent="geoapiExercises")
    location = geolocator.geocode(f"{city}, {country}")
    return location.latitude, location.longitude
