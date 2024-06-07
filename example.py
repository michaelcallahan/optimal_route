from optimal_route.main import main

region = "California"
start_city = "San Francisco"
end_city = "San Diego"
country = "USA"
mpg = 25  # miles per gallon
tank_volume = 15  # gallons
fos = 1.5 # fill when 66% depleted

optimal_stops = main(region, start_city, end_city, country, mpg, tank_volume, fos)
print(optimal_stops)
