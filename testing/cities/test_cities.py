import unittest
from city_functions import get_formatted_city_name

class CityTestCase(unittest.TestCase):
    '''tests for city_functions.py'''

    def test_city_country(self): 
        formatted_city = get_formatted_city_name('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')
    
    def test_city_country_popultation(self):
        formatted_city = get_formatted_city_name('paris', 'france', 2000000)
        self.assertEqual(formatted_city, 'Paris, France - population 2000000')

if __name__ == '__main__':
    unittest.main()