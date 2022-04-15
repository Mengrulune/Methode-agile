from town import Town
from pythonProject.country import Country
import unittest

class TownTestCase(unittest.TestCase):
    def test_gdp_town(self):
        town = Town("Paris", 38, 2_000_000)
        country = Country('France', [town])
        result = town.contribution_in_gdp_country()
        self.assertEqual(0.038, result)

class CountryTestCase(unittest.TestCase):
    def test_gdp_country(self):
        town_1 = Town("Paris", 38, 2_000_000)
        town_2 = Town("Lyon", 25, 500_000)
        country = Country('France', [town_1, town_2])
        result = country.gdp_country()
        self.assertEqual(88500000, result)


