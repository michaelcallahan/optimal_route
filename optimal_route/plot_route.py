import folium
from folium.plugins import MarkerCluster
from optimal_route.main import main


def plot_route(route_coords, gas_stations, optimal_stops, start_coords, end_coords):
    mid_lat = (start_coords[0] + end_coords[0]) / 2
    mid_lng = (start_coords[1] + end_coords[1]) / 2
    m = folium.Map(location=[mid_lat, mid_lng], zoom_start=7)

    folium.PolyLine([(coord[1], coord[0]) for coord in route_coords], color='blue', weight=2.5, opacity=1).add_to(m)

    gas_station_cluster = MarkerCluster(name='Gas Stations').add_to(m)
    for gas_station in gas_stations:
        folium.Marker(location=[gas_station[0], gas_station[1]],
                      icon=folium.Icon(color='gray', icon='info-sign')).add_to(gas_station_cluster)

    for stop in optimal_stops:
        folium.Marker(location=[stop[0], stop[1]], icon=folium.Icon(color='red', icon='info-sign')).add_to(m)

    folium.Marker(location=start_coords, popup="Start: " + str(start_coords), icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=end_coords, popup="End: " + str(end_coords), icon=folium.Icon(color='blue')).add_to(m)

    folium.LayerControl().add_to(m)
    m.save('../html/route_map.html')


if __name__ == "__main__":
    region = "California"
    start_city = "San Francisco"
    end_city = "San Diego"
    country = "USA"
    mpg = 25
    tank_volume = 15
    fos = 1.5

    optimal_stops, route_coords, gas_stations, start_coords, end_coords = main(region, start_city, end_city, country,
                                                                               mpg, tank_volume, fos)
    plot_route(route_coords, gas_stations, optimal_stops, start_coords, end_coords)
