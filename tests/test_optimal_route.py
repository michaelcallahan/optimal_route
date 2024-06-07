import unittest
from optimal_route.main import main


class TestOptimalRoute(unittest.TestCase):
    def test_route(self):
        region = "California"
        start_city = "San Francisco"
        end_city = "San Diego"
        country = "USA"
        mpg = 25
        tank_volume = 15
        fos = 1.5

        optimal_stops, route_coords, gas_stations, start_coords, end_coords = main(region,
                                                                                   start_city,
                                                                                   end_city,
                                                                                   country,
                                                                                   mpg,
                                                                                   tank_volume,
                                                                                   fos)
        self.assertIsInstance(optimal_stops, list)
        self.assertGreater(len(optimal_stops), 0)


if __name__ == "__main__":
    unittest.main()
