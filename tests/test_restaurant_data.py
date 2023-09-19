'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DO NOT EDIT THIS FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

from cmath import exp
import io
from unittest import mock, TestCase

from restaurant_data import *


class TestRestaurantData(TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_explore_data(self, mock_stdout):
        explore_data()

        expected = "https://www.yelp.com/biz/four-barrel-coffee-san-francisco\n37.7670169511878 -122.42184275\n"
        expected += "375 Valencia St, San Francisco, CA, 94113\n"

        self.assertEqual(expected, mock_stdout.getvalue())

    @mock.patch('builtins.input', side_effect=['Islands', '10848 W Pico Blvd', 'Tortilla Soup'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_favorite_restaurant(self, mock_stdout, mock_input):
        favorite_restaurant()

        expected = "{'name': 'Islands', 'address': '10848 W Pico Blvd', 'favorite_dish': 'Tortilla Soup'}\n"
        expected += "{'name': 'Islands', 'address': '10848 W Pico Blvd'}\n"
        expected += "116th & Broadway, NY 10016\n"

        self.assertEqual(expected, mock_stdout.getvalue())

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_clean_print(self, mock_stdout):
        clean_print()

        expected = "name: Four Barrel Coffee\nurl: https://www.yelp.com/biz/four-barrel-coffee-san-francisco\n"
        expected += "latitude: 37.7670169511878\nlongitude: -122.42184275\ncity: San Francisco\ncountry: US\n"
        expected += "state: CA\naddress: 375 Valencia St\nzip_code: 94113\ndistance: 1604.23\ntransactions: ['pickup', 'delivery']\n"

        self.assertEqual(expected, mock_stdout.getvalue())
