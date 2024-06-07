import argparse
from geopy.distance import geodesic
from optimal_route.geo_utils import get_city_coordinates
from optimal_route.gas_stations import get_gas_stations
from optimal_route.routing import calculate_route


def find_optimal_gas_stations(route_coords, gas_stations, mpg, tank_volume, fos):
    max_distance = mpg * tank_volume * 1.60934 / fos  # Convert miles to kilometers
    current_distance = 0
    stops = []

    for i in range(len(route_coords) - 1):
        start_coord = route_coords[i]
        end_coord = route_coords[i + 1]
        segment_distance = geodesic((start_coord[1], start_coord[0]), (end_coord[1], end_coord[0])).kilometers
        current_distance += segment_distance

        if current_distance >= max_distance:
            closest_station = None
            min_distance_to_station = float('inf')
            for station in gas_stations:
                distance_to_station = geodesic((end_coord[1], end_coord[0]), station).kilometers
                if distance_to_station < min_distance_to_station:
                    min_distance_to_station = distance_to_station
                    closest_station = station

            if closest_station:
                stops.append(closest_station)
                current_distance = 0  # Reset distance after refueling

    return stops


def main(region, start_city, end_city, country, mpg, tank_volume, fos):
    start_coords = get_city_coordinates(start_city, country)
    end_coords = get_city_coordinates(end_city, country)
    gas_stations = get_gas_stations(region)
    route_coords, total_distance = calculate_route(start_coords, end_coords)

    optimal_stops = find_optimal_gas_stations(route_coords, gas_stations, mpg, tank_volume, fos)

    print(f"Total Distance: {total_distance} km")
    print(f"Number of Stops: {len(optimal_stops)}")
    for i, stop in enumerate(optimal_stops):
        print(f"Stop {i + 1}: {stop}")

    return optimal_stops, route_coords, gas_stations, start_coords, end_coords


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find optimal gas station stops.")
    parser.add_argument("--region", required=True, help="Region to search for gas stations.")
    parser.add_argument("--start_city", required=True, help="Starting city.")
    parser.add_argument("--end_city", required=True, help="Ending city.")
    parser.add_argument("--country", required=True, help="Country of the cities.")
    parser.add_argument("--mpg", type=float, required=True, help="Miles per gallon of the car.")
    parser.add_argument("--tank_volume", type=float, required=True, help="Gas tank volume in gallons.")
    parser.add_argument("--tank_volume", type=float, required=True, help="Factor of safety for tank capacity.")

    args = parser.parse_args()
    main(args.region, args.start_city, args.end_city, args.country, args.mpg, args.tank_volume)
