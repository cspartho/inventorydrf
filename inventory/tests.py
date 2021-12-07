from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestApi(APITestCase):
    def test_url_api(self):
        url = '/api/inventory/'
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.status_code, 200, f'expected Response code 200, instead get {response.status_code}')

class TestUrls(TestCase):
    def test_list(self):
        response = self.client.get(reverse('inventory_list'))   
        self.assertEqual(response.status_code, 200,f'expected Response code 200, instead get {response.status_code}')
    
    def test_details(self):
        response = self.client.get(reverse('inventory_detail',kwargs={"pk":2}))
        self.assertEqual(response.status_code, 200,f'expected Response code 200, instead get {response.status_code}')
        

    
