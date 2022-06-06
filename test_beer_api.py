#!/usr/bin/env python

from unittest import TestCase
from requests import Session


class TestBeerAPI(TestCase):

    def setUp(self):
        self.base_url = 'https://api.punkapi.com'
        self.api_version = 'v2'
        self.route = 'beers'
        self.query = 'brewed_after=12-2015'
        session = Session()
        self.response = session.get(f'{self.base_url}/{self.api_version}/{self.route}?{self.query}')
        self.data = []
        if self.response.status_code == 200:
            self.data = self.response.json()

    def test_response_code_should_be_ok(self):
        expected = 200
        self.assertEqual(self.response.status_code, expected, 'HTTP response code should be OK')

    def test_response_not_empty(self):
        expected = 0
        self.assertGreater(len(self.data), expected, 'result set is empty')

    def test_abv_property_validation(self):
        for beer in self.data:
            self.assertIn('abv', beer, 'property not exist')
            self.assertTrue(beer['abv'] != '',
                            'abv is empty string')  # this assert can be excluded because it's covered in line 36
            self.assertIsNotNone(beer['abv'],
                                 'abv is None')  # this assert can be excluded because it's covered in line 36
            # self.common_checks('abv', beer)
            self.assertTrue(type(beer['abv']) is float, 'abv is not float')
            self.assertGreater(beer['abv'], 4, 'abv is <= 4')

    def test_name_property_validation(self):
        for beer in self.data:
            self.common_checks('name', beer)

    def common_checks(self, name, beer):
        self.assertIn(name, beer, f'property {name} is not exist')
        self.assertTrue(beer[name] != '',
                        f'{name} is empty string')
        self.assertIsNotNone(beer[name],
                             f'{name} is None')
