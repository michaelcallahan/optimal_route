import requests

def get_gas_stations(region):
    url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    area[name="{region}"]->.searchArea;
    (
      node["amenity"="fuel"](area.searchArea);
    );
    out body;
    """
    response = requests.get(url, params={'data': query})
    data = response.json()
    gas_stations = []
    for element in data['elements']:
        if 'lat' in element and 'lon' in element:
            gas_stations.append((element['lat'], element['lon']))
    return gas_stations
